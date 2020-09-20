from db_settings import Base
from sqlalchemy import Column, Integer, String, DateTime

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    video_id = Column(String(255), nullable=False)
    comment_id = Column(String(255), nullable=False)
    author_name = Column(String(255), nullable=False)
    url = Column(String(1024), nullable=False)
    comment = Column(String(2056), nullable=False)
    date = Column(DateTime, nullable=False)
    like_count = Column(Integer, default=0)
    sentiment = Column(String(1024), nullable=False)
    
    def __str__(self):
        if len(self.comment) > 40:
            cut_comment = self.comment[:40] + '...'
        else:
            cut_comment = self.comment
        return f"<Comment by {self.author_name}: {cut_comment}>"