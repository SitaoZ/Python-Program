## pandas 使用集合


- 去除指定行
```bash
# 选择数字列（排除 Geneid 和 gene_symbol）
numeric_cols = df.select_dtypes(include=['number']).columns

# 保留所有数字列绝对值都 >= 1 的行（每一列都要满足）
filtered_df = df[df[numeric_cols].abs().ge(1).all(axis=1)]

# 保留至少有一个数字列绝对值 >= 1 的行
filtered_df = df[df[numeric_cols].abs().ge(1).any(axis=1)]


# 如果你知道具体的数字列名称（跳过前两列）
numeric_cols = df.columns[2:]  # 假设前两列是 Geneid 和 gene_symbol
# 保留至少有一个数字列绝对值 >= 1 的行
filtered_df = df[df[numeric_cols].abs().ge(1).any(axis=1)]


# 删除所有数字列绝对值都小于1的行
numeric_cols = df.select_dtypes(include=['number']).columns
filtered_df = df[~df[numeric_cols].abs().lt(1).all(axis=1)]

```
