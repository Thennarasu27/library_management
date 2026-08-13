frappe.pages['page1'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'My Page',
        single_column: true
    });

    $(page.body).html(`
        <h2>Welcome</h2>
        <button class="btn btn-primary">Click Me</button>
    `);
	$(page.title).html(`title:hello`);
	
}