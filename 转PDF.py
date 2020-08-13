from win32com.client import Dispatch, constants, gencache

docx_path = 'f:/pycharm/word6用python把word转为PDF/客户1-价格通知.docx'
pdf_path = 'f:/pycharm/word6用python把word转为PDF/客户1-价格通知.pdf'

#gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)

wd = Dispatch("Word.Application")

doc = wd.Documents.Open(docx_path, ReadOnly=1)
doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF, Item=constants.wdExportDocumentWithMarkup,
                        GreateBookmarks=constants.wdExportCreateHeadingBookmarked)
wd.Quit(constants.wdDoNotSaveChanges)
