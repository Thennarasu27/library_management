def boot_session(bootinfo):
    print("Library Management: extend_bootinfo hook executed")

    bootinfo["library_management"] = {
        "message": "Hello from Library Management"
    }