import { registry } from "@web/core/registry";

function createVolume(name, width, depth, height) {
    // Return steps to create a volume in your interface
    // Find documentation on 
    // https://www.odoo.com/documentation/18.0/developer/reference/backend/testing.html?highlight=tour#javascript
    return [];
}

registry.category("web_tour.tours").add("tour_create_volumes", {
    // 1. Create 5 volumes
    // 2. Check that dimensions are corrects (here you test also the widget)
    // 3. Remove one record
    // 4. Update one record
    steps: () => [],
});
