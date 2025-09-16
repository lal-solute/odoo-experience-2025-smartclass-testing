# ./odoo-bin --config=../.vscode/odoo.conf -u smartclass --test-enable --test-tags=:TestVolume

import odoo.tests


@odoo.tests.tagged('post_install', '-at_install')
class TestVolume(odoo.tests.HttpCase):

    def test_volume_model(self):
        # Create at leat 3 volumes and check that their volumes and categories are as expected.
        # Adapt function in your model to test that:
        # - When volume is 0, category is small
        # - When volume is 0.86, category is small
        # - When volume is 0.99, category is small
        # - When volume is 1, category is small
        # - When volume is 1.00000001, category is medium
        # - When volume is 100, category is medium
        # - When volume is 101, category is large
        # - When volume is 1000 category is large
        return True

    def test_tour_create_volumes(self):
        # Create a start_tour function that use your tour added in registry web_tour.tours
        # Add few asertions to ensure created volumes are in database and that their dimensions are corrects.
        return True
