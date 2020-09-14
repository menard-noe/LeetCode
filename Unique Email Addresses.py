from typing import List
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_mail = set()

        for email in emails:
            local_name, domain = str.split(email, '@')

            local_name = str.replace(local_name, '.', '')
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]

            set_mail.add(local_name + '@' + domain)

        return len(set_mail)


if __name__ == "__main__":
    # execute only if run as a script
    input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solution = Solution()
    print(solution.numUniqueEmails(input))