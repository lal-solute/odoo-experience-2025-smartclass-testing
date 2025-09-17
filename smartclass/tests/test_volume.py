# ./odoo-bin --config=../.vscode/odoo.conf -u smartclass --test-enable --test-tags=:TestVolume

import odoo.tests


@odoo.tests.tagged('post_install', '-at_install')
class TestVolume(odoo.tests.HttpCase):

    def test_volume_model(self):
        volume0 = self.env["smartclass.volume"].create({
            "name": "volume 0",
            "width": 2.56,
            "height": 1.34,
        })
        self.assertEqual(volume0.volume, 0)
        self.assertEqual(volume0.category, "small")
        volume1 = self.env["smartclass.volume"].create({
            "name": "volume 1",
            "depth": 1,
            "width": 1,
            "height": 0.2,
        })
        self.assertEqual(volume1.volume, 0.2)
        self.assertEqual(volume1.category, "small")
        volume2 = self.env["smartclass.volume"].create({
            "name": "volume 2",
            "depth": 7.24,
            "width": 2.56,
            "height": 1.34,
        })
        self.assertAlmostEqual(volume2.volume, 24.84, places=2)
        self.assertEqual(volume2.category, "medium")
        volume3 = self.env["smartclass.volume"].create({
            "name": "volume 3",
            "depth": 100,
            "width": 10,
            "height": 10,
        })
        self.assertAlmostEqual(volume3.volume, 10000, places=2)
        self.assertEqual(volume3.category, "large")

    def test_tour_create_volumes(self):
        # Create a start_tour function that use your tour added in registry web_tour.tours
        # Add few asertions to ensure created volumes are in database and that their dimensions are corrects.
        return True
