# 実装中につき特筆すべき事項なし

# 計画
Makefileを用いて実行(全員分のデータのダウンロード)

**順序**
- Makefile(./project)
- get_token.py(./project)
- get_option.py
- download.sh
- get_token.py
- base_data.py(csv -> pkl)

# 現状
nobu -> MacbookPro GoogleChrome
chikako -> MacbookPro Firefox
yota -> MacbookPro Firefox DeveloperEdition

## **編集中**
`project/project_nobu/lib/Get_*_HeartRate.py`
 月ごとに分けているのでyearだけ別で関数を作成して手動もしくは自動的かを決定する->projectにget_option.pyを作成してMakefileで実行
 順序としてはget_tokenの次にする