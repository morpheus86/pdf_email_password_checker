import PyPDF2

# rb mode means read binary=> allow to read pdf in binary
with open("dummy.pdf", mode="rb") as file:
    reader = PyPDF2.PdfFileReader(file)  # get the fileby reading it
    read = reader.getPage(0)  # get a specific page on the file
    page = read.rotateCounterClockwise(90)  # rotate the page using page class object method
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', "wb") as new_file:
        writer.write(new_file)


