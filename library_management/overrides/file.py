# def before_write(**kwargs):
#     print("FILE IS ABOUT TO BE WRITTEN")

# # def write_file(*args, **kwargs):
# #     print("My custom write_file() is running")

# def delete_file(*args, **kwargs):
#     print("CUSTOM DELETE FILE")
#     print("ARGS:", args)
#     print("KWARGS:", kwargs)

def before_write_file(*args, **kwargs):
    print("Library Management: before_write_file hook executed")
def write_file(*args, **kwargs):
    print("Library Management: write_file hook executed")
def delete_file(*args, **kwargs):
    print("Library Management: delete_file hook executed")