# calculation-tools-api
https://calculation-tools.vercel.app/  
↑のAPIになります。

# Dockerでの動作確認
### step1: プロジェクトのクローン
`git clone https://github.com/ryu-0729/calculation-tools-api.git`
### step2: Dockerイメージのビルド
`docker build -t 任意のイメージ名 .`
### step3: Dockerコンテナの起動
`docker run -d --name 任意のコンテナ名 -p 80:80 step2でビルドしたイメージ名`

# Swagger
http://127.0.0.1/docs
