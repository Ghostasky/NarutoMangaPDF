from PIL import Image
import os


def combine2Pdf(folderPath, pdfFilePath):
    files = os.listdir(folderPath)
    pngFiles = []
    sources = []
    # print(files)
    for file in files:
        if 'jpg' in file:
            pngFiles.append(folderPath + file)
    pngFiles.sort()
    print(pngFiles)
    output = Image.open(pngFiles[0])
    pngFiles.pop(0)
    print(pngFiles)
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGBA":
            pngFile = pngFile.convert("RGBA")
        sources.append(pngFile)
    output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)


if __name__ == "__main__":
    list = []
    for i in range(33, 73):
        list.append(i)
    folder_list = []
    pdf_list = []
    for i in list:
        folder = "./[岸本齊史][火影忍者][NARUTO -ナルト- ][東立][DL].Vol.{}/".format(i)
        folder_list.append(folder)
        pdf = "./{}.pdf".format(i)
        pdf_list.append(pdf)
    for i in range(len(folder_list)):
        folder = folder_list[i]
        pdf = pdf_list[i]

        combine2Pdf(folder, pdf)
        print(folder, pdf, " finish!")
