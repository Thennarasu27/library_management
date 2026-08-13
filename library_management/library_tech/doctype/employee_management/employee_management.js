frappe.ui.form.on("Employee Management", {
    refresh(frm) {
        frm.add_custom_button("Testing", () => {
            frappe.call({
                method:"library_management.library_tech.doctype.employee_management.employee_management.utility2",
                args:{
                    'doc':"Employee Management"},
                callback(r) {
                    console.log(0);
                    frappe.msgprint(r.message);
                }
            });

        });

    }
});
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
