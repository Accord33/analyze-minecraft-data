# マインクラフト研究用
プログラムを実行する場合はsrcファイルをカレントディレクトリにして実行してください
## 推奨ファイル構成
```
.
├── src
│   ├── getIP.py # マイクラのログデータからipを取り出す
│   ├── stasAnaly.py # plan_users.csvからプレイヤーネームとuuidを取り出す→jsonファイルを読み込み必要なデータを取り出しcsvに書き込む
│   └── ungzip.py # ログデータがgzipに圧縮されているので一斉解凍する
├── logs
│   └── マインクラフトのログデータを入れてください
├── stats
│   └── マイクラのstatsの中身を入れてください
├── entity_data
│   ├── enemy # 敵モブのエンティティIDが記載
│   └── friend # 友好モブのエンティティIDが記載
└── ex_data
    └── plan_users.csv # planのplan_usersというテーブルのcsvデータを入れてください
```
