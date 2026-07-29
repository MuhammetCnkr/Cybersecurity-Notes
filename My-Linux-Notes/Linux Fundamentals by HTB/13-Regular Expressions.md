---
Date: 2026-07-27 10:04
category:
tags:
Tools:
---

| **Operators** | **Description**                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `(a)`         | The round brackets are used to group parts of a regex. Within the brackets, you can define further patterns which should be processed together.                             |
| `[a-z]`       | The square brackets are used to define character classes. Inside the brackets, you can specify a list of characters to search for.                                          |
| `{1,10}`      | The curly brackets are used to define quantifiers. Inside the brackets, you can specify a number or a range that indicates how often a previous pattern should be repeated. |
| `\|`          | Also called the OR operator and shows results when one of the two expressions matches                                                                                       |
| `.*`          | Operates similarly to an AND operator by displaying results only when both expressions are present and match in the specified order                                         |

# Or Operator:
- Suppose we use the `OR` operator. The regex searches for one of the given search parameters. In the next example, we search for lines containing the word `my` or `false`. To use these operators, you need to apply the extended regex using the `-E` option in grep.
```bash
grep -E "(my|false)" /etc/passwd
# İçinde my veya false olan çıktıları basar
```
# And Operator:
- Since one of the two search parameters always occurs in the three lines, all three lines are displayed accordingly. However, if we use the `AND` operator, we will get a different result for the same search parameters.
```bash
grep -E "(my.*false)" /etc/passwd
# Burada içinde hem my olan hem false olanı basar
```

# RegEx:
- Standart `grep` komutunda bazı özel karakterleri (örneğin `|`, `+`, `?`, `()`) tanıyabilmesi için önüne ters eğik çizgi (`\`) koyman gerekir (`\|` gibi). `grep -E` (ya da kısaca `egrep`) kullandığında ise bu karakterler **doğrudan özel anlamlarıyla** çalışır. Yani karmaşık arama kalıplarını kaçış karakteri (`\`) kalabalığı olmadan, çok daha temiz yazabilirsin.
- ![[Screenshot 2026-07-27 at 10.42.38.png]]