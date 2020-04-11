import PyPDF2

with open("super.pdf", "rb") as file:  # can also use file=PyPDF2.PdfFileReader=(open("super.pdf", "rb))
    reader = PyPDF2.PdfFileReader(file)
    num_pages = reader.getNumPages()
    idx = 0
    output = PyPDF2.PdfFileWriter()
    with open("wtr.pdf", "rb") as new_file:
        watermark = PyPDF2.PdfFileReader(new_file)
        while idx < num_pages:
            page = reader.getPage(idx)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
            with open("watermark.pdf", "wb") as watermarked:
                output.write(watermarked)
            idx += 1

# Simpler way

# temp = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
# watermarked_file = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
# result = PyPDF2.PdfFileWriter()
# number_page = temp.getNumPages()
#
# def merge_into_one(num_page, template, watermark, output):
#     for i in range(num_page)
#         page = template.getPage(i)
#         page.mergePage(watermark.getPage(0))
#         output.addPage(page)
#         with open("watermark.pdf", "wb") as watermarked:
#             output.write(watermarked)
#
# merge_into_one(number_page, temp, watermarked_file, result)
