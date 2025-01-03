from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class SoundBase(SQLModel):
    name: str= Field(index= True)
    description: str| None= None
    
class Sound(SoundBase, table= True):
    id: str| None= Field(primary_key= True)
    file_dir: str
    created_at: datetime= Field(default_factory= datetime.now)

    tags: list['Tag']= Relationship(back_populates= 'sounds')
    
class SoundCreate(SoundBase):
    ...
    
class SoundOutput(SoundBase):
    tags: list['Tag']
    created_at: datetime
    
class TagBase(SQLModel):
    name: str
    description: str
    
class Tag(TagBase, table= True):
    id: int| None= Field(default= None, primary_key= True)

    sounds: list[Sound]| None= Relationship(back_populates= 'tags')
    