// frappe.ui.form.on("Employee Management", {
//     refresh(frm) {
//         frm.add_custom_button("Testing", () => {
//             frappe.call({
//                 method:"library_management.library_tech.doctype.employee_management.employee_management.utility2",
//                 args:{
//                     'doc':"Employee Management"},
//                 callback(r) {
//                     console.log(0);
//                     frappe.msgprint(r.message);
//                 }
//             });

//         });

//     }
// });
// frappe.pages['Employee Management'].on_page_load = function(wrapper) {

    

// };

// controls:
// frappe.ui.form.on("Employee Management",{
//     refresh(frm){
//         frappe.ui.form.make_control({
//         parent:frm.fields_dict.control.$wrapper,
//         df: {
//             label: 'Due Date',
//             fieldname: 'due_date',
//             fieldtype: 'Date'
//         },
//         render_input: true
//     });
//     }
// })

//common utilities
// frappe.ui.form.on('Employee Management', {
//     refresh(frm) {
//         //console.log("hello")
//         //console.log("route : "+frappe.get_route());
//         //frappe.set_route('practice');
// let result = frappe.format(
//         50000,
//         { fieldtype: 'Currency' }
//         );

//         console.log("result :"+ result);

//     }
// });


// dialog api 

frappe.ui.form.on('Employee Management',{
    refresh(frm)
    {
        
//             let d = new frappe.ui.Dialog({
//         title: 'Enter details',

//         fields: [
//             {
//                 label: 'First Name',
//                 fieldname: 'first_name',
//                 fieldtype: 'Data'
//             },
//             {
//                 label: 'Last Name',
//                 fieldname: 'last_name',
//                 fieldtype: 'Data'
//             },
//             {
//                 label: 'Age',
//                 fieldname: 'age',
//                 fieldtype: 'Int'
//             }
//         ],

//         primary_action_label: 'Submit',

//         primary_action(values) {
//             console.log(values);
//             d.hide();
//         }
//     });

// d.show();
        //frappe.throw("Error");
        // frappe.prompt('name1',({value})=>
        // {
        //     console.log(value);
        // })
        //frappe.confirm("Proceed?",()=>{console.log("Yes")},()=>{console.log("No")})
        //frappe.warn('Are you sure you want to proceed?','There are unsaved changes on this page',() => {console.log("Pressed Continue")},'continue',true);
        // frappe.show_alert({
        //     message:__('Hi, you have a new message'),
        //     indicator:'green'
        // }, 5);
        // frappe.show_progress('Loading..', 70, 100, 'Please wait');
        //frappe.confirm("Open New Form?",()=>{frappe.new_doc("Leave")},()=>{console.log("No")})
        // new frappe.ui.form.MultiSelectDialog({
        // doctype: "Employee Management",
        // action(selections) {
        // console.log(selections);
        // frm.add_custom_button("Select Employees", () => {

        //     new frappe.ui.form.MultiSelectDialog({  //not working
        //         doctype: "Employee Management",
        //         target: frm,

        //         action(selections) {
        //             console.log("Selected employees:", selections);
        //         }
        //     });

        // });
        // }});
        //         let d = new frappe.ui.Dialog({
        //     title: "Project Employees",

        //     fields: [
        //         {
        //             fieldname: "table1",
        //             fieldtype: "Table",
        //             label: "Employees",

        //             fields: [
        //                 {
        //                     fieldname: "name",
        //                     label: "Name",
        //                     fieldtype: "Data",
        //                     in_list_view: 1
        //                 }
        //             ]
        //         }
        //     ],

        //     primary_action_label: "Submit",

        //     primary_action(values) {
        //         console.log(values.table1);
        //         d.hide();
        //     }
        // });

        // d.show();

        //scanner API
        frm.add_custom_button("Scan", () => {
            new frappe.ui.Scanner({
                dialog: true,
                multiple: false,
                on_scan(data) {
                    frappe.msgprint(
                        "Scanned Value: " + data.decodedText
                    );
                }
            });
        });
    }

    //scanner API
    
})

// Copyright (c) 2026, Thennarasu M and contributors
// For license information, please see license.txt 
// frappe.ui.form.on("Employee Management", {
// 	refresh(frm) {
// 	},
// });
// function check(frm) {
//         if(!frm.doc.name1)
//             {frm.disable_save();}
//         else
//         {
//             frm.enable_save();
//         } 
//     }
// function checksal(frm)
// {
//     if(!frm.doc.salary)
//     {
//         frm.toggle_enable("salary",true);
//     }
//     else
//     {
//         frm.set_df_property("salary","read_only",1);
//         frm.toggle_enable("salary",false);
//         frm.refresh_field("salary");
//         frm.toggle_display("salary",false);
//     }
// }
// frappe.ui.form.on("Employee Management",
// {
//     setup(frm) {
//         console.log("SETUP", frm.doc.name);
//         frappe.msgprint("setup");},
//     before_load(frm) {
//         console.log("BEFORE_LOAD", frm.doc.name);
//         frappe.msgprint("before load");},
//     onload(frm) {
//         frappe.msgprint("onload");
//         console.log("ONLOAD", frm.doc.name);},
//     refresh(frm) {
//         frm.add_custom_button("Show Selected", () => {
//         let selected = frm.get_selected();
//         console.log(selected);
//         frappe.msgprint(JSON.stringify(selected));});
//         frm.add_custom_button("Hello", () => {
//             frm.call({
//             method: "say_hello",
//             callback(r) {
//                 frappe.msgprint(r.message);}});});
//         if(frm.is_new())
//         {frappe.msgprint("newone");}
//         frm.toggle_reqd("salary",true);
//         frappe.msgprint("refresh");
//         console.log("REFRESH", frm.doc.name);
//         check(frm);
//         frm.add_custom_button("Trigger",()=>{
//             frm.trigger("do");
//         })
//          frm.add_custom_button("Send Email", () => {
//             frm.doc.name1="the";
//             frm.refresh_field("name1");
//             frm.dirty();
//             if(!frm.doc.name1)
//             {frm.set_intro("Name empty");}
//             frappe.msgprint("Email button clicked");});
//             frm.email_doc();
//             checksal(frm);
//         frm.change_custom_button_type("Send Email",null,"primary");
//         //frm.remove_custom_button("Send Email");
//         //frm.clear_custom_buttons();
//         frm.set_query("links",()=>
//         {
//             return{
//                 filters:
//                 {
//                     items:"item1"
//                 }
//             };
//         });
//         frm.add_child("table1",
//             {
//             pro1:"p1",
//             pro2:"p2"
//             });
//         frm.refresh_field("table1");
//         },
//     do(frm)
//         {
//             frappe.msgprint("triggered");
//         },
//     name1(frm)
//     {
//         if(frm.is_dirty())
//         {
//             frappe.msgprint("save it");
//         }
//         check(frm);
        
//     },
//     salary(frm)
//     {
//         checksal(frm);
        
//     },
//     onload_post_render(frm)
//     {
//         frappe.msgprint("onload-post");
//     },
//     validate(frm)
//     {
//         if(frm.doc.name1==="Thennarasu")
//         {
//             frappe.throw("Hello bro");
//         }
//     },
//     before_save(frm)
//     {
//         frm.doc.name1=frm.doc.name1.toUpperCase();
//     },
//     after_save(frm)
//     {
//         frappe.show_alert(
//             {
//                 message:"Saved Successfully",
//                 indicator:"blue"
//             }
//         );
//     },
//     after_discard(frm) 
//     {
//     frappe.show_alert({
//         message: "Changes Discarded",
//         indicator: "orange"
//     });
//     },
//     timeline_refresh(frm) {
//         console.log("Timeline Refreshed");

//         frappe.show_alert({
//             message: "Timeline Refreshed",
//             indicator: "green"
//         });
//     },
//     table1_on_form_rendered(frm)
//     {
//         frappe.msgprint("Hello");
//     },
//     name1(frm)
//     {
//         frappe.msgprint("hello changed");
//         frm.set_value("designation","hello").then(()=>
//     {
//         frappe.msgprint("set-value");
//     })
//     },
//     salary(frm)
//     {
//         frappe.msgprint("sal-changed");
//         //frm.refresh();
//         //frm.save();
//     }
// }
// );

// frappe.ui.form.on("Projectsemp", {

//     table1_add(frm, cdt, cdn) {
//         frappe.msgprint("Row Added");
//     },

//     before_table1_remove(frm, cdt, cdn) {
//         frappe.msgprint("About to Remove");
//     },

//     table1_remove(frm, cdt, cdn) {
//         frappe.msgprint("Row Removed");
//     },

//     table1_move(frm, cdt, cdn) {
//         frappe.msgprint("Row Moved");
//     },

//     // form_render(frm, cdt, cdn) {
//     //     frappe.msgprint("Child Form Opened");
//     // }

// });
// frappe.ui.form.on("Employee Management", {
//     refresh(frm) {

//         let parent = frm.fields_dict.parent1.$wrapper;

//         let control = frappe.ui.form.make_control({
//             parent: parent,
//             df: {
//                 fieldtype: "Data",
//                 label: "Employee Name",
//                 fieldname: "emp_name"
//             },
//             render_input: true
//         });

//     }
// });

//form tours
// frappe.ui.form.on('Employee Management', {
//     onload(frm) {
//         const tour_name = 'Custom Field';

//         frm.tour.init({ tour_name }).then(() => {
//             frm.tour.start();
//         });
//     }
// });

//server calls
// frappe.ui.form.on("Employee Management", {
//     refresh(frm) {
//         frappe.call("library_management.api.func5")
//             .then(r => {
//                 frappe.msgprint(r);
//                 console.log(r);
//             });
//     }
// });

//background jobs 
        // frappe.call("library_management.api.start_job").then(r=>{
        //     frappe.msgprint(r);
        // })

// frappe.ui.form.on("Employee Management",{
//     refresh(frm){
//         // frm.add_custom_button("Set Status",()=>{
//         //     //frm.set_value("name1","Changed")
//         //     doc.name1="changed"
//         //     doc.save()
//         //     frm.refresh_field("name1")
//         //     frappe.msgprint("Changed")
//         // })
//         if(frm.doc.status==="pending")
//             {
//                 frm.add_custom_button("Approve",()=>
//                 {
//                     frm.set_value('status','approved')
//                     frm.refresh_field("status");
//                     frappe.msgprint("Done");
//                     //frm.remove_custom_button("Approved")
//                 })
//             }
//     }
// })
frappe.ui.form.on("Employee Management", {
    refresh(frm) {
        let d = new frappe.ui.Dialog({
            title: "Enter First Name:",
            fields: [
                {
                    label: "Name",
                    fieldname: "name1",
                    fieldtype: "Data"
                }
            ],
            primary_action_label:'submit',
            primary_action(values)
            {
                val=values.name1
                frappe.new_doc('task_assign',{name1:val})
                d.hide()
            }
        });

        d.show();
    }
});
