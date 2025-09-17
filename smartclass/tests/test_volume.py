# ./odoo-bin --config=../.vscode/odoo.conf -u smartclass --test-enable --test-tags=:TestVolume

import odoo.tests


@odoo.tests.tagged('post_install', '-at_install')
class TestVolume(odoo.tests.HttpCase):

    def test_volume_model(self):
        # Create at leat 3 volumes and check that their volumes and categories are as expected.
        # Adapt function in your model to test that:
        volume_zero = self.env["smartclass.volume"].create([{"name": "small", "depth": 0, "height": 0, "width": 0}])
        volume_small_1 = self.env["smartclass.volume"].create([{"name": "small1", "depth": 0.95, "height": 0.95, "width": 0.95}])
        volume_small_2 = self.env["smartclass.volume"].create([{"name": "small2", "depth": 0.995, "height": 0.995, "width": 0.995}])
        volume_small_3 = self.env["smartclass.volume"].create([{"name": "small3", "depth": 1, "height": 1, "width": 1}])
        # - When volume is 0, category is small
        # - When volume is 0.86, category is small
        # - When volume is 0.99, category is small
        # - When volume is 1, category is small
        # - When volume is 1.00000001, category is medium
        # - When volume is 100, category is medium
        # - When volume is 101, category is large
        # - When volume is 1000 category is large
        self.assertEqual(0, volume_zero.volume)
        self.assertEqual("small", volume_zero.category)

        self.assertEqual(0.86, volume_small_1.volume)
        self.assertEqual("small", volume_small_1.category)

        self.assertEqual(0.99, volume_small_2.volume)
        self.assertEqual("small", volume_small_2.category)

        self.assertEqual(1, volume_small_3.volume)
        self.assertEqual("small", volume_small_3.category)
        return True

    def test_tour_create_volumes(self):
        # Create a start_tour function that use your tour added in registry web_tour.tours
        # Add few asertions to ensure created volumes are in database and that their dimensions are corrects.
        return True
