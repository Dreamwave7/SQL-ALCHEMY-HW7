from learn import User, Articles, session

# userq = User(name = "Dima lisovoy2")
# session.add(userq)
# print(userq.id)
# session.commit()

# art = Articles(title = "My city2", content = "I live in Kyiv2", user_id = userq.id)
# session.add(art)
# session.commit()

#READING=================================================================================

# user = session.query(User).filter_by(name = "Dima lisovoy2").scalar()
# print(user.id, user.name)


#UPDATE==================================================================================
art = session.query(Articles).get(1)
art.content = "Ichange the content"
session.commit()
print(art.content)






















