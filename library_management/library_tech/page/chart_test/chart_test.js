frappe.pages["chart_test"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Chart Test",
        single_column: true
    });

    $(wrapper).find(".layout-main-section").html(`
        <div id="chart" style="margin-top: 30px;"></div>
    `);

    const data = {
        datasets: [
            {
                name: "Some Data",
                values: [10, 20, 15, 30, 25]
            }
        ]
    };

    let chart = new frappe.ui.RealtimeChart(
        "#chart",
        "test_event",
        8,
        {
            title: "My Realtime Chart",
            data: data,
            type: "line",
            height: 250,
            colors: ["#7cd6fd"]
        }
    );

};