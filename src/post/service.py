from src.db.main import init_db


class postService:
    async def getAllUser():
        statement = await init_db.prisma.post.find()
        return statement