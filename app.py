from flask import Flask, render_template

app = Flask(__name__)

# --- データ管理 ---
salon_name = "Peu a peu" 

catchphrase_title = "あなただけの色を、少しずつ。"
catchphrase_body = """
“Peu à peu” はフランス語で「少しずつ」。<br>
昨日より今日、今日より明日。<br>
あなたの魅力が少しずつ花開く、<br>
そんなヘアスタイルを一緒に見つけます。
"""

menu_groups = [
    {
        "category": "カット",
        "item_list": [
            {"name": "大人", "price": "¥3,000"},
            {"name": "高校生", "price": "¥2,000"},
            {"name": "小学生", "price": "¥1,500"},
        ]
    },
    {
        "category": "トリートメント",
        "item_list": [
            {"name": "", "price": "¥1,500"},
        ]
    },
    {
        "category": "パーマ",
        "item_list": [
            {"name": "", "price": "¥4,000"},
        ]
    },
    {
        "category": "ストレートパーマ",
        "item_list": [
            {"name": "全体", "price": "¥8,000"},
            {"name": "ロング", "price": "¥10,000"},
            {"name": "部分", "price": "¥5,000"},
        ]
    },
    {
        "category": "カラー",
        "item_list": [
            {"name": "全体", "price": "¥6,000"},
            {"name": "部分", "price": "¥4,000"},
            {"name": "ヘナ", "price": "¥4,000"},
        ]
    },
]

addon_note = "主張サロン: +¥700"
tax_note = "（消費税込み）"

cat_section_title = "看板猫について"
cat_section_body = """
当サロンには、看板猫がおります。<br>
施術スペースには入ってきませんので、猫アレルギーの方もどうぞご安心ください。<br>
猫がお好きな方はどうぞお気軽にお声がけください。
"""

@app.route('/')
def index():
    # ★猫のデータをHTMLに渡す部分を追加
    return render_template('index.html', 
                           salon_name=salon_name,
                           catchphrase_title=catchphrase_title,
                           catchphrase_body=catchphrase_body,
                           menu_groups=menu_groups,
                           addon_note=addon_note,
                           tax_note=tax_note,
                           cat_section_title=cat_section_title,
                           cat_section_body=cat_section_body)

@app.route('/pricelist')
def price_list_page():
    return render_template('pricelist.html', 
                           salon_name=salon_name, 
                           menu_groups=menu_groups,
                           addon_note=addon_note,
                           tax_note=tax_note)

if __name__ == '__main__':
    app.run(debug=True)