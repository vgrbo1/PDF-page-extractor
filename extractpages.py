from PyPDF2 import PdfReader,PdfWriter
import sys
import datetime
argv = sys.argv
reader = PdfReader(argv[1])
writer = PdfWriter()
l = len(argv)

if(l >= 2):
    ok = True
    for i in range(2, len(argv)):
        try:
            writer.add_page(reader.pages[int(argv[i])-1])
        except Exception:
            print("You have specified incorrect page number: ",argv[i])
            ok = False
            break
    

    if(ok):
        str = "ExtractedPages-" + datetime.date.today().strftime("%d-%m-%Y") + ".pdf"
        with open(str, "wb") as iz:
            writer.write(iz)

        print("Done!")

else:
    print("You haven't specified the pages you want to extract!")
