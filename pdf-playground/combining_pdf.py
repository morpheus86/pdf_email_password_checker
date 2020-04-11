import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merging = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merging.append(pdf)
    merging.write("super.pdf")


pdf_combiner(inputs)
