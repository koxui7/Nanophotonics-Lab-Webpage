import tempfile
import unittest
from unittest import mock

from scripts.mirror_site import crawl_site, extract_links, local_path_for_url, normalize_url


class MirrorSiteTests(unittest.TestCase):
    def test_normalize_url_drops_fragments_and_resolves_relative_links(self):
        base_url = "https://photonlab.hajim.rochester.edu/research1.html"
        self.assertEqual(
            normalize_url(base_url, "../research2.html#about-section"),
            "https://photonlab.hajim.rochester.edu/research2.html",
        )

    def test_extract_links_collects_html_assets_and_css_urls(self):
        html = """
        <html>
          <head>
            <link rel="stylesheet" href="css/style.css">
            <style>.hero { background-image: url('img/banner.jpg'); }</style>
          </head>
          <body>
            <a href="research1.html#about-section">Research</a>
            <img src="img/team/01.jpg">
            <script src="js/site.js"></script>
          </body>
        </html>
        """
        links = extract_links("https://photonlab.hajim.rochester.edu/", html)
        self.assertIn("https://photonlab.hajim.rochester.edu/research1.html", links)
        self.assertIn("https://photonlab.hajim.rochester.edu/css/style.css", links)
        self.assertIn("https://photonlab.hajim.rochester.edu/img/banner.jpg", links)
        self.assertIn("https://photonlab.hajim.rochester.edu/img/team/01.jpg", links)
        self.assertIn("https://photonlab.hajim.rochester.edu/js/site.js", links)

    def test_local_path_for_url_keeps_html_and_asset_structure(self):
        root = "/tmp/photonlab"
        self.assertEqual(
            local_path_for_url(root, "https://photonlab.hajim.rochester.edu/"),
            "/tmp/photonlab/photonlab.hajim.rochester.edu/index.html",
        )
        self.assertEqual(
            local_path_for_url(
                root,
                "https://photonlab.hajim.rochester.edu/img/team/01.jpg",
            ),
            "/tmp/photonlab/photonlab.hajim.rochester.edu/img/team/01.jpg",
        )

    def test_crawl_site_logs_failed_assets_without_aborting(self):
        html = """
        <html>
          <head><link rel="stylesheet" href="css/style.css"></head>
          <body><img src="img/missing.png"></body>
        </html>
        """

        class FakeResponse:
            def __init__(self, url, status_code, content, content_type):
                self.url = url
                self.status_code = status_code
                self.content = content
                self.headers = {"Content-Type": content_type}

            @property
            def text(self):
                return self.content.decode("utf-8")

            def raise_for_status(self):
                if self.status_code >= 400:
                    import requests

                    raise requests.exceptions.HTTPError(f"{self.status_code} for {self.url}")

        responses = {
            "https://photonlab.hajim.rochester.edu/": FakeResponse(
                "https://photonlab.hajim.rochester.edu/",
                200,
                html.encode("utf-8"),
                "text/html",
            ),
            "https://photonlab.hajim.rochester.edu/css/style.css": FakeResponse(
                "https://photonlab.hajim.rochester.edu/css/style.css",
                200,
                b"body{color:black;}",
                "text/css",
            ),
            "https://photonlab.hajim.rochester.edu/img/missing.png": FakeResponse(
                "https://photonlab.hajim.rochester.edu/img/missing.png",
                404,
                b"not found",
                "text/html",
            ),
        }

        def fake_get(url, timeout):
            return responses[url]

        with tempfile.TemporaryDirectory() as tmpdir:
            with mock.patch("requests.Session.get", side_effect=fake_get):
                manifest = crawl_site(
                    "https://photonlab.hajim.rochester.edu/",
                    tmpdir,
                    max_pages=10,
                )

        self.assertIn(
            "https://photonlab.hajim.rochester.edu/css/style.css",
            manifest["visited"],
        )
        self.assertIn(
            "https://photonlab.hajim.rochester.edu/img/missing.png",
            manifest["failed"],
        )

    def test_crawl_site_logs_connection_errors_without_aborting(self):
        html = '<html><body><img src="img/reset.png"></body></html>'

        class FakeResponse:
            def __init__(self, url, content):
                self.url = url
                self.status_code = 200
                self.content = content
                self.headers = {"Content-Type": "text/html"}

            @property
            def text(self):
                return self.content.decode("utf-8")

            def raise_for_status(self):
                return None

        def fake_get(url, timeout):
            if url.endswith("reset.png"):
                import requests

                raise requests.exceptions.ConnectionError("connection reset")
            return FakeResponse(url, html.encode("utf-8"))

        with tempfile.TemporaryDirectory() as tmpdir:
            with mock.patch("requests.Session.get", side_effect=fake_get):
                manifest = crawl_site(
                    "https://photonlab.hajim.rochester.edu/",
                    tmpdir,
                    max_pages=10,
                )

        self.assertIn(
            "https://photonlab.hajim.rochester.edu/img/reset.png",
            manifest["failed"],
        )


if __name__ == "__main__":
    unittest.main()
