# -*-coding:UTF-8-*-
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
from interpretation_of_laws import Ui_Dialog
import os
import re
import shutil
from pdf2image import convert_from_path
from bs4 import BeautifulSoup


class main_windows(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choice_laws()  # 法規選單
        self.exit_event()  # 取消事件
        self.checkBrowse.clicked.connect(self.get_file)  # 點擊瀏覽
        self.choice_article()
        self.checkOK.clicked.connect(self.ok_event)
        self.show()

    def choice_laws(self):
        # 法規項目下拉選單
        choices = ['勞工安全衛生管理辦法', '勞動檢查法', '無條文項目',
                   '營造安全衛生設施標準', '職業安全衛生法',
                   '職業安全衛生教育訓練規則', '職業安全衛生管理辦法']
        self.regulation.addItems(choices)
        # 判定選擇了什麼法
        self.regulation.currentText()

        # 離開按鈕

    def exit_event(self):
        self.checkCancel.clicked.connect(QApplication.instance().quit)

    # 取得要匯入檔案位置
    def get_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "選擇PDF檔案", "", "PDF files(*.pdf)", options=options)
        self.label.setText(filename)

    # 讀取法規條例
    def choice_article(self):
        article = "第{}條".format(self.article.value())
        return article

    def ok_event(self):
        """正則"""
        # 資料夾名稱正則
        file_regex = r'[^/]+[.$]'

        file_name = self.label.text()

        file_matches = re.finditer(file_regex, file_name)

        for matchNum, match in enumerate(file_matches, start=1):
            browse_name = match.group()[:-1]

        # herf取數字正則
        herf_num_regex = r'[0-9]'

        herf_chinese_regex = r'[\D]'

        herf_name = browse_name

        herf_num_matches = ''.join(re.findall(herf_num_regex, herf_name))

        herf_chinese_matches = ''.join(re.findall(herf_chinese_regex, herf_name))
        """PDF converter2 JPG"""
        pdf_name = self.label.text()
        pages = convert_from_path(pdf_name, 500, poppler_path='C:/poppler-0.68.0/bin')
        for page_number, page in enumerate(pages):
            page.save(pdf_name[:-4] + str(page_number) + '.jpg', "JPEG")
            break

        """選擇匯入"""
        if self.label.text() != "麻煩請先點選瀏覽選擇要匯入的檔案":
            print(self.label.text())
            path = 'G:/法規分類/{}/第{}條'.format(self.regulation.currentText(), self.article.value())
            if os.path.isdir("G:/法規分類/{}/第{}條/{}".format(self.regulation.currentText(), self.article.value(),
                                                         browse_name)):
                QMessageBox.about(self, "失敗", "已有重複資料，請確認是否已存在檔案或洽詢管理者")
            elif not os.path.isdir(path):
                os.mkdir('G:/法規分類/{}/第{}條'.format(self.regulation.currentText(), self.article.value()))
                os.mkdir('G:/法規分類/{}/第{}條/{}'.format(self.regulation.currentText(), self.article.value(), browse_name))
                os.mkdir('G:/法規分類/{}/第{}條/{}/images'.format(self.regulation.currentText(), self.article.value(),
                                                            browse_name))
                shutil.copy2(self.label.text(),
                             "G:/法規分類/{}/第{}條/{}".format(self.regulation.currentText(), self.article.value(),
                                                         browse_name))
                shutil.move(self.label.text()[:-4] + "0" + '.jpg',
                            'G:/法規分類/{}/第{}條/{}/images'.format(self.regulation.currentText(), self.article.value(),
                                                               browse_name))
                QMessageBox.about(self, "恭喜", "已成功匯入檔案，請至G:/法規分類/{}/第{}條/{}查看".format(self.regulation.currentText(),
                                                                                      self.article.value(),
                                                                                      browse_name))
            elif os.path.isdir(path):
                os.mkdir('G:/法規分類/{}/第{}條/{}'.format(self.regulation.currentText(), self.article.value(), browse_name))
                os.mkdir('G:/法規分類/{}/第{}條/{}/images'.format(self.regulation.currentText(), self.article.value(),
                                                            browse_name))
                shutil.copy2(self.label.text(),
                             "G:/法規分類/{}/第{}條/{}".format(self.regulation.currentText(), self.article.value(),
                                                         browse_name))
                shutil.move(self.label.text()[:-4] + "0" + '.jpg',
                            'G:/法規分類/{}/第{}條/{}/images'.format(self.regulation.currentText(), self.article.value(),
                                                               browse_name))

                QMessageBox.about(self, "恭喜", "已成功匯入檔案，請至G:/法規分類/{}/第{}條/{}查看".format(self.regulation.currentText(),
                                                                                      self.article.value(),
                                                                                      browse_name))
        """各條文轉換字典"""
        laws_dict = {
            '勞工安全衛生管理辦法': 'LSHA',
            '勞動檢查法': 'LIA',
            '營造安全衛生設施標準': 'SCSHI',
            '職業安全衛生法': 'OSHA',
            '職業安全衛生教育訓練規則': 'OSHETR',
            '職業安全衛生管理辦法': 'OSHM',
            '無條文項目': 'NoneLaw'
        }

        """BeautifulSoup抓取HTML片段"""

        # 讀取檔案
        with open('G:\法規分類\營造業歷年法規解釋查詢.html', 'r', encoding='UTF-8') as info:
            txt = info.read()
        soup = BeautifulSoup(txt, 'html.parser')
        print(self.article.value())
        # 左側選單
        title = soup.find(id='{}{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))  # 尋找的ID
        # if title is None:

        tag_a = soup.new_tag('a')
        tag_a['herf'] = "#{}+A".format(herf_num_matches)
        tag_a.string = '{}'.format(herf_chinese_matches)
        title.li.a.insert_before(tag_a)

        # 寫入法規查詢
        info = open('G:\法規分類\營造業歷年法規解釋查詢.html', 'w', encoding='UTF-8')
        info.write(soup.prettify())
        info.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_windows()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
