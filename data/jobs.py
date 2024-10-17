# import uuid
#
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
#
#
# class DBBase(DeclarativeBase):
#     pass
#
# class JobDBThing(DBBase):
#     __tablename__ = "jobs"
#
#     id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
#     name: Mapped[str] = mapped_column(nullable=False, unique=False)
#     #status: Mapped[Enum(Status)] = mapped_column(enum=Status, nullable=False, unique=False)
