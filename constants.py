CACHE_HOST = "direct.learnpython.org"
DB_HOST = "direct.learnpython.org"
SECRET_KEY = "this is a secret. really."

LEARNPYTHON_DOMAIN = "learnpython.org"
LEARNCPP_DOMAIN = "learn-cpp.org"
LEARNJS_DOMAIN = "learn-js.org"
LEARNCS_DOMAIN = "learncs.org"
LEARNSQL_DOMAIN = "learnsql"
LEARNLINUX_DOMAIN = "learnlinux"


from collections import OrderedDict

DOMAIN_DATA = OrderedDict()

DOMAIN_DATA[LEARNPYTHON_DOMAIN] = {
        "language" : "python",
        "language_id": 116,
        "codemirror_mode": "python",
        "prism_mode": "language-python",
        "analytics" : "UA-22741967-1",
        "language_uppercase" : "Python",
        "default_code" : """# Welcome to the Interactive Python Tutorial.
# Start by choosing a chapter and
# write your code in this window.

print("Hello, World!")
    """
}

DOMAIN_DATA[LEARNJS_DOMAIN] = {
        "language" : "javascript",
        "language_id": 35,
        "codemirror_mode": "text/javascript",
        "prism_mode": "language-javascript",
        "analytics" : "UA-22741967-5",
        "language_uppercase" : "JavaScript",
        "default_code" : """// Welcome to the Interactive JavaScript Tutorial.
// Start by choosing a chapter and
// write your code in this window.

console.log("Hello, World!");
"""
}

DOMAIN_DATA[LEARNCS_DOMAIN] = {
        "language" : "c#",
        "language_id": 27,
        "codemirror_mode": "text/x-csharp",
        "prism_mode": "language-csharp",
        "analytics" : "UA-22741967-10",
        "language_uppercase" : "C#",
        "default_code" : """// Welcome to the Interactive C# Tutorial.
// Start by choosing a chapter and write your code in this window.

using System;

public class Hello
{
    public static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}
""",
        "container_word" : "class",
        "container_indent" : "        ",
        "container" : """using System;
using System.Collections.Generic;

public class Hello
{
    public static void Main()
    {
{code}
    }
}
""",
}

DOMAIN_DATA[LEARNCPP_DOMAIN] = {
        "language" : "c++11",
        "language_id": 1,
        "codemirror_mode": "text/x-csrc",
        "prism_mode": "language-cpp",
        "analytics" : "UA-22741967-12",
        "language_uppercase" : "C++",
        "default_code" : """// Welcome to the Interactive C++ Tutorial.
// Start by choosing a chapter and
// write your code in this window.

#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
    """,
        "container_word" : "main()",
        "container_indent" : "    ",
        "container" : """#include <iostream>
using namespace std;

int main() {
{code}
return 0;
}
"""
}

DOMAIN_DATA[LEARNSQL_DOMAIN] = {
        "language" : "sql",
        "language_id": 000,
        "codemirror_mode": "sql",
        "prism_mode": "language-sql",
        "analytics" : "",
        "language_uppercase" : "SQL",
        "default_code" : ""
}

DOMAIN_DATA[LEARNLINUX_DOMAIN] = {
        "language" : "linux",
        "language_id": 000,
        "codemirror_mode": "linux",
        "prism_mode": "language-linux",
        "analytics" : "",
        "language_uppercase" : "Linux",
        "default_code" : ""
}


# this will run once
for domain, v in list(DOMAIN_DATA.items()):
    # TODO: Update domain data here

    if domain == "learnpython.org":
        v["namespace"] = domain
        v["full_url"] = "/en/Welcome"
        v["contact_email"] = "admin@" + v["namespace"]
        v["support_email"] = "support@" + v["namespace"]

        v["logo"] = "/static/img/logos/" + v["namespace"] + ".png"
        v["share_logo"] = "/static/img/share-logos/" + v["namespace"] + ".png"
        v["favicon"] = "/static/img/favicons/" + v["namespace"] + ".ico"
        v["styled_domain"] = domain
        v["sender"] = "%s <%s>" % (domain, v["contact_email"])
    else:
        v["namespace"] = domain
        v["full_url"] = "/under-construction"
        v["contact_email"] = "admin@" + v["namespace"]
        v["support_email"] = "support@" + v["namespace"]

        v["logo"] = "/static/img/logos/" + v["namespace"] + ".png"
        v["share_logo"] = "/static/img/share-logos/" + v["namespace"] + ".png"
        v["favicon"] = "/static/img/favicons/" + v["namespace"] + ".ico"
        v["styled_domain"] = domain
        v["sender"] = "%s <%s>" % (domain, v["contact_email"])

    import os
    if not os.path.exists(v["logo"][1:]):
        raise Exception("no logo for %s - %s" % (domain, v["logo"][1:]))
    if not os.path.exists(v["share_logo"][1:]):
        raise Exception("no share logo for %s - %s" % (domain, v["share_logo"][1:]))
    if not os.path.exists(v["favicon"][1:]):
        raise Exception("no favicon for %s - %s" % (domain, v["favicon"][1:]))



