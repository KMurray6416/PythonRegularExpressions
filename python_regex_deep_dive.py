import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
                                          #using negative lookahead to extract all emails
                                          #so long as this group is not positioned here
print(emails)