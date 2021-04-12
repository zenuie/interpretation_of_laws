# -*-coding:UTF-8-*-
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
from interpretation_of_laws import Ui_Dialog
import os
import re
import shutil
from pdf2image import convert_from_path
from bs4 import BeautifulSoup, Comment

# 各名詞標籤
'''
pdf檔名           |herf_name=browse_name
pdf檔名純數字部分  |herf_num_matches
法規名稱          |self.regulation.currentText()
法規英文名稱       |laws_dict[self.regulation.currentText()]
法規條例          |self.article.value()


'''


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
        choices = ['勞工安全衛生管理辦法', '勞動檢查法',
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
            path = 'P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條'.format(self.regulation.currentText(),
                                                                       self.article.value())
            if os.path.isdir("P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}".format(self.regulation.currentText(),
                                                                                    self.article.value(),
                                                                                    browse_name)):
                QMessageBox.about(self, "失敗", "已有重複資料，請確認是否已存在檔案或洽詢管理者")
                quit()
            elif not os.path.isdir(path):
                os.mkdir('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條'.format(self.regulation.currentText(),
                                                                             self.article.value()))
                os.mkdir('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}'.format(self.regulation.currentText(),
                                                                                self.article.value(), browse_name))
                os.mkdir('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}/images'.format(self.regulation.currentText(),
                                                                                       self.article.value(),
                                                                                       browse_name))
                shutil.copy2(self.label.text(),
                             "P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}".format(self.regulation.currentText(),
                                                                                    self.article.value(),
                                                                                    browse_name))
                shutil.move(self.label.text()[:-4] + "0" + '.jpg',
                            'P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}/images'.format(self.regulation.currentText(),
                                                                                          self.article.value(),
                                                                                          browse_name))

            elif os.path.isdir(path):
                os.mkdir('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}'.format(self.regulation.currentText(),
                                                                                self.article.value(), browse_name))
                os.mkdir('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}/images'.format(self.regulation.currentText(),
                                                                                       self.article.value(),
                                                                                       browse_name))
                shutil.copy2(self.label.text(),
                             "P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}".format(self.regulation.currentText(),
                                                                                    self.article.value(),
                                                                                    browse_name))
                shutil.move(self.label.text()[:-4] + "0" + '.jpg',
                            'P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}/images'.format(self.regulation.currentText(),
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
        with open('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/營造業歷年法規解釋查詢.html', 'r', encoding='UTF-8') as info:
            txt = info.read()
        soup = BeautifulSoup(txt, 'html.parser')
        laws_comment = soup.new_string("{}第{}條".format(self.regulation.currentText(), self.article.value()), Comment)
        # 左側選單
        if soup.find(id='{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value())) is None:

            """左側選單html新增項目框架"""
            li_div = soup.new_tag('li', attrs={
                'id': '{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value())})
            a_laws = soup.new_tag('a', attrs={
                'href': '#{}{}'.format(laws_dict[self.regulation.currentText()], self.article.value()),
                'class': 'nav-header collapsed',
                'data-toggle': 'collapse'})
            a_laws.string = '第{}條'.format(self.article.value())
            span = soup.new_tag('span', attrs={'class': 'pull-right glyphicon glyphicon-chevron-down'})
            ul = soup.new_tag('ul', attrs={
                'id': '{}{}'.format(laws_dict[self.regulation.currentText()], self.article.value()),
                'class': 'nav nav-list collapse thridmenu',
                'style': 'height: 0px;'})
            li = soup.new_tag('li')
            a = soup.new_tag('a', attrs={'href': '#{}A'.format(herf_num_matches)})
            a.string = '{}'.format(herf_name)

            """右側主畫面html新增項目框架"""
            h4 = soup.new_tag('h4')
            h4.string = '第{}條'.format(self.article.value())
            right_div = soup.new_tag('div', attrs={
                'id': 'main{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value())})
            right_li_div = soup.new_tag('li')
            right_li_div.string = ('{}'.format(herf_name))
            right_ul = soup.new_tag('ul', attrs={'id': '{}A'.format(herf_num_matches)})
            right_a = soup.new_tag('a', attrs={'target': '_blank',
                                               'href': './{}\第{}條\{}\{}.pdf'.format(self.regulation.currentText(),
                                                                                    self.article.value(), herf_name,
                                                                                    herf_name)})
            right_img = soup.new_tag('img', attrs={
                'src': './{}\第{}條\{}\images\{}0.jpg'.format(self.regulation.currentText(), self.article.value(),
                                                            herf_name, herf_name), 'width': '200%'})
            """選單html判斷前後"""
            for laws_num in range(self.article.value(), 0, -1):
                if soup.find(id='{}no{}'.format(laws_dict[self.regulation.currentText()],
                                                laws_num)) and self.article.value() > laws_num or laws_num == 1:
                    if laws_num == 1:
                        title = soup.find(id='{}'.format(laws_dict[self.regulation.currentText()]))
                        title.insert(1, laws_comment)
                        title.insert(1, li_div)
                        main_laws = soup.find(id='main{}'.format(laws_dict[self.regulation.currentText()]))
                        main_laws.insert(1, right_div)
                    else:
                        title = soup.find(id='{}no{}'.format(laws_dict[self.regulation.currentText()], laws_num))
                        title.insert_after(li_div)
                        main_laws = soup.find(
                            id='main{}no{}'.format(laws_dict[self.regulation.currentText()], laws_num))
                        main_laws.insert_after(right_div)
                    insert_law = soup.find(
                        id='{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))
                    right_insert_law = soup.find(
                        id='main{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))
                    insert_law.insert_before(laws_comment)
                    insert_law.insert(1, a_laws)
                    insert_law.a.insert(1, span)
                    insert_law.insert(1, ul)
                    insert_law.ul.insert(1, li)
                    insert_law.ul.li.insert(1, a)
                    right_insert_law.insert_before(h4)
                    right_insert_law.insert(1, right_li_div)
                    right_insert_law.li.insert(1, right_ul)
                    right_insert_law.li.ul.insert(1, right_a)
                    right_insert_law.li.ul.a.insert(1, right_img)
                    break
        else:
            title = soup.find(id='{}{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))
            laws = soup.new_tag('a', attrs={'href': '#{}A'.format(herf_num_matches)})
            laws.string = '{}'.format(herf_name)
            title.li.a.insert_after(laws)
            """右邊主選單條文已存在"""
            right_title = soup.find(
                id='main{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))
            right_li_div = soup.new_tag('li')
            right_li_div.string = ('{}'.format(herf_name))
            right_ul = soup.new_tag('ul', attrs={'id': '{}A'.format(herf_num_matches)})
            right_a = soup.new_tag('a', attrs={'target': '_blank',
                                               'href': './{}\第{}條\{}\{}.pdf'.format(self.regulation.currentText(),
                                                                                    self.article.value(), herf_name,
                                                                                    herf_name)})
            right_img = soup.new_tag('img', attrs={
                'src': './{}\第{}條\{}\images\{}0.jpg'.format(self.regulation.currentText(), self.article.value(),
                                                            herf_name, herf_name), 'width': '200%'})
            right_title.insert(1, right_li_div)
            right_title = soup.find(
                id='main{}no{}'.format(laws_dict[self.regulation.currentText()], self.article.value()))
            right_title.li.insert(1, right_ul)
            right_title.li.ul.insert(1, right_a)
            right_title.li.ul.a.insert(1, right_img)

        """寫入法規查詢"""
        info = open('P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/營造業歷年法規解釋查詢.html', 'w', encoding='UTF-8')
        info.write(soup.prettify())
        info.close()
        QMessageBox.about(self, "恭喜", "已成功匯入檔案，請至P:/營造安全科(第二科)/營造安全法令釋疑/營造業歷年法規解釋查詢/{}/第{}條/{}查看".format(
            self.regulation.currentText(),
            self.article.value(),
            browse_name))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_windows()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
