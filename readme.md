1. клонування репизиторію

```bash
git clone https://github.com/your-username/fastapi-blog.git
cd fastapi-blog

2. pip install -r requirements.txt
3. перед запуском сервера
```powershell
$env:PYTHONPATH = "."
python app/init_db.py

3. uvicorn main:app --reload

