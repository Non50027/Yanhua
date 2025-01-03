import asyncio, os, uuid
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from sqlmodel import Session, select
from server.models import get_session
from server.models.db_sound import Sound, SoundCreate, SoundOutput, Tag

router= APIRouter()

FILE_DIR= 'D:\\Yanhua\\static\\sounds\\'

# 存入音效
@router.post('/upload', response_model= SoundOutput)
async def upload(file_data: SoundCreate, file: UploadFile, tag: list[str], session: Session= Depends(get_session)):
    print('file dir', os.getenv('VITE_STATIC'))
    file_id= str(uuid.uuid4())
    new_file_name= f"{file_data.name}_{file_id}.{file.filename.split('.')[-1]}"
    file_path= os.path.join(FILE_DIR, new_file_name)
    
    # 儲存檔案
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        
    tags= [session.exec(select(Tag).where(Tag.name== tag_name)).one() for tag_name in tag]
    
    data= Sound(
        name= file_data.name,
        description= file_data.description,
        file_dir= file_path,
        tags= tags
    )
    session.add(data)
    session.commit()
    return data

@router.get('/all-sound', response_model= list[SoundOutput])
async def get_all_sound(session: Session= Depends(get_session)):
    all_data= session.exec(select(Sound)).all()
    return all_data