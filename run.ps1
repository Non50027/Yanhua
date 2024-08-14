
& .\.venv\Scripts\Activate.ps1

switch ($args[0]) {
    # 預設行為2
    "" {
        Push-Location .\frontend
        Start-Process -NoNewWindow -FilePath "cmd" -ArgumentList "/c yarn dev"
        Pop-Location
        
        python .\backend\manage.py makemigrations $args[1]
        python .\backend\manage.py migrate $args[1]
        python .\backend\manage.py runserver
        Start-Sleep -Seconds 5
        & $MyInvocation.InvocationName # 重新運行腳本本身
    }
    # 生成 freezefile.txt
    "-f" {
        pip freeze > freezefile.txt
    }
    # 安裝 freezefile.txt 中的包
    "-i" {
        pip install -r freezefile.txt
    }
    # 遷移資料庫
    "-m" {
        python .\backend\manage.py makemigrations $args[1]
        python .\backend\manage.py migrate $args[1]
    }
    default {
        Write-Host "未知的參數: $args[0]"
    }
}
