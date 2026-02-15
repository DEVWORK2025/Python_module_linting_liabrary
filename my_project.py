import format_logfile as f

###print(f.filename)

try:
    a= int(input("enter the number"))
except ValueError:
    l, file_obj = f.add_files()
    print(l, file_obj)
    l.addHandler(file_obj)
    l.error("Number shld entered")
