# 啟動虛擬環境
& .\\.venv\\Scripts\\Activate.ps1

function Start-NewProcess {
    param(
        [string]$process_name,
        [string]$command
    )
    # 獲取當前工作目錄
    $current_directory = Get-Location

    Start-Process -NoNewWindow -PassThru -FilePath "wt" -ArgumentList "-w 0 new-tab -p `"PowerShell`" --title `"$process_name`" -- pwsh -Command `"cd $current_directory && & .\\.venv\\Scripts\\Activate.ps1 && $command && cmd /c exit`""
    Start-Sleep -Seconds 1
}

Start-NewProcess -process_name "Frontend" -command "cd .\\frontend && yarn dev --host --port 5330"
Start-NewProcess -process_name "Backend" -command "cd .\\backend && python .\\manage.py makemigrations && python .\\manage.py migrate && python .\\manage.py runserver 0.0.0.0:8330"
Start-NewProcess -process_name "Uvicorn" -command "python .\\run_uvicorn.py"

# switch ($args[0]) {
#     # 預設行為
#     "" {
#         # 啟動前端
#         Push-Location .\frontend
#         Start-Process -NoNewWindow -FilePath "cmd" -ArgumentList "/c yarn dev --host --port 5330" 
#         Pop-Location
        
#         # 執行 Django 的遷移並啟動後端
#         python .\\backend\\manage.py makemigrations $args[1]
#         python .\\backend\\manage.py migrate $args[1]
#         python .\\backend\\manage.py runserver 0.0.0.0:8330

#     }
#     # 生成 freezefile.txt
#     "-f" {
#         pip freeze > freezefile.txt
#     }
#     # 安裝 freezefile.txt 中的包
#     "-i" {
#         pip install -r freezefile.txt
#     }
#     # 遷移資料庫
#     "-m" {
#         python .\\backend\\manage.py makemigrations $args[1]
#         python .\\backend\\manage.py migrate $args[1]
#     }
#     default {
#         Write-Host "未知的參數: $args[0]"
#     }
# }
