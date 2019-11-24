<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
# 人工智能导论作业 Chapter 3, 7, 8, 9

PB17121687

虞佳焕

## 3.6

### (a)

- 状态：所有区域的着色状态。
- 初始状态：所有区域未着色。
- 目标测试：所有区域着色，没有两个相邻的区域颜色相同。
- 后继函数：给一个区域着色
- 代价函数：着色区域的数量

### (b)

- 状态：箱子与猴子的布局
- 初始状态：猴子和箱子的初始布局
- 目标测试：猴子吃到香蕉
- 后继函数：猴子跳上箱子、猴子跳下箱子、猴子将箱子从一个地点推到另一个地点、猴子从一个地点走到另一个地点、获得香蕉
- 代价函数：操作数量

### (c)

- 状态：当前已检查的记录的数量
- 初始状态：未检查任何记录
- 目标测试：找到非法的记录
- 后继函数：按顺序检查下一个记录
- 代价函数：检查的记录数量

### (d)

- 状态：三个水壶的水量 (a,b,c)
- 初始状态 (0,0,0)
- 目标测试：(1,0,0) 或 (0,1,0) 或 (0,0,1)
- 后继函数：用外部水装满一个瓶，或倒空一个瓶，或者选定倒出瓶 x 和倒入瓶 y, 从 x 倒水到 y 直到 x 变空或者 y 变满。
- 代价函数：操作数量。

## 7.6

### (a)

真。由单调性显然可证。

### (b)

真。如果在 $\alpha$ 的每个模型中 $\beta \wedge\gamma$ 为真，则在这些模型中，$\beta$ 和 $\gamma$ 也为真。

### (c)

假。$\beta\equiv A$, $\gamma\equiv\neg A$ 为反例。

## 7.14

### (a)

(ii) 是正确的。

### (b)

都是。

## 7.18

### (a)

| Food  | Party | Drinks | 句子 |
| ----- | ----- | ------ | ---- |
| true  | true  | true   | true |
| true  | true  | false  | true |
| true  | false | true   | true |
| true  | false | false  | true |
| false | true  | true   | true |
| false | true  | false  | true |
| false | false | true   | true |
| false | false | false  | true |

所以句子是有效的。

### (b)

$\implies$ 的左边有

$$\begin{aligned}
& (Food \implies  Party) \vee  (Drinks \implies  Party) \\
& (\neg Food \vee  Party) \vee  (\neg Drinks \vee  Party) \\
& (\neg Food \vee  Party \vee  \neg Drinks \vee  Party) \\
& (\neg Food \vee  \neg Drinks \vee  Party)
\end{aligned}$$

右边有

$$\begin{aligned}
& (Food \wedge  Drinks) \implies  Party \\
& \neg (Food \wedge  Drinks) \vee  Party \\
& (\neg Food \vee  \neg Drinks) \vee  Party \\
& (\neg Food \vee  \neg Drinks \vee  Party)
\end{aligned}$$

两侧写成 CNF 是相同的。

### (c)

原句子取反

$$\begin{aligned}
& \neg [[(Food \implies  Party) \vee  (Drinks \implies  Party)] \implies  [(Food \wedge  Drinks) \implies  Party]] \\
& [(Food \implies  Party) \vee  (Drinks \implies  Party)] \wedge  \neg [(Food \wedge  Drinks) \implies  Party] \\
& [ (\neg Food \vee  \neg Drinks \vee  Party) \wedge  Food \wedge  Drinks \wedge  \neg Party
\end{aligned}$$

显然最后一个句子是不可满足的。因此原句子是有效的。

## 8.8

不能得出，需要补充定理

$$\forall  x, y, z\ Spouse(x, z) \wedge  Spouse(y, z) \implies  x=y$$

如果 Spouse 是一元函词，那么问题变为是否可以从 $Jim \neq George$ 和 $Spouse(Laura)= Jim$ 中推出 $\neg Spouse(Laura)=George$.

答案显然是“可以”。

## 8.13

### (a)

$$\begin{aligned}
& \forall  s\ Breezy(s) \implies \exist r\ Adjacent(r, s) \wedge  Pit(r) \\
& \forall  s\ \neg Breezy(s) \implies  \neg \exist  r\ Adjacent(r, s) \wedge  Pit(r)
\end{aligned}$$

可以导出

$$\forall  s \exist  r\ Adjacent(r, s) \wedge  Pit(r) \implies  Breezy(s)$$

于是可以导出

$$\forall  s\ Breezy(s) \iff \exist r\ Adjacent(r, s) \wedge  Pit(r)$$

### (b)

$$\forall  s\ Pit(s) \implies  [\forall  r\ Adjacent(r, s) \implies  Breezy(r)]$$

这条语句允许风自发产生而周围没有陷阱（“没有陷阱导致周围没有风”并不正确）。只需补充一句“如果所有周围方块都没有陷阱，那么这个方块没有风”。

$$\forall  s\ [\forall r\ Adjacent(r, s) \implies  \neg Pit(r)] \implies  \neg Breezy(s)$$

## 8.28

### (a)

$$W(G,T)$$

### (b)

$$\neg W(G,E)$$

### (c)

$$W(G,T) \vee W(M,T)$$

### (d)

$$\exist s\ W(J, s)$$

### (e)

$$\exist x\ C(x,R) \wedge  O(J, x)$$

### (f)

$$\forall s\ S(M,s, R) \implies  W(M,s)$$

### (g)

$$\neg [\exist s\ W(G, s) \wedge \exist p\ S(p, s, R)]$$

### (h)

$$\forall s\ W(G, s) \implies \exist p, a\ S(p, s, a)$$

### (i)

$$\exist  a\ \forall s\ W(J, s) \implies \exist p\ S(p, s, a)$$

### (j)

$$\exist  d, a, s\ C(d, a) \wedge O(J, d) \wedge  S(B,T, a)$$

### (k)

$$\forall  a\ [\exist s\ S(M,s, a)] \implies \exist d\ C(d, a) \wedge  O(J, d)$$

### (l)

$$\forall  a\ [\forall s, p\ S(p, s, a) \implies  S(B, s, a)] \implies \exist d\ C(d, a) \wedge  O(J, d)$$

## 9.4

### (a)

$$\{x/A, y/B, z/B\}$$

### (b)

无解。

### (c)

$$\{y/John, x/John\}$$

### (d)

无解。

## 9.9

### (a)

```
Goal G0: 7 ≤ 3+ 9               Resolve with (8) {x1/7,z1/3+ 9}
    Goal G1: 7 ≤ y1             Resolve with (4) {x2/7,y1/7+ 0}.Succeeds
    Goal G2: 7+ 0 ≤ 3+ 9        Resolve with (8) {x3/7+ 0,z3/3+ 9}
        Goal G3: 7+ 0 ≤ y3      Resolve with (6) {x4/7,y4/0,y3/0+ 7} Succeeds
        Goal G4: 0+ 7 ≤ 3+ 9    Resolve with (7) {w5/0,x5/7,y5/3,z5/9}
            Goal G5: 0 ≤ 3      Resolve with (1) Succeeds
            Goal G6: 7 ≤ 9      Resolve with (2) Succeeds
        G4 succeeds
    G2 succeeds
G0 succeeds
```

### (b)

从 (1), (2), (7) $\{w/0,x/7,y/3,z/9\}$ 导出 (9) $0+ 7 ≤ 3+ 9$

从 (9), (6), (8) $\{x1/0,y1/7,x2/0 + 7,y2/7 + 0,z2/3+ 9\}$ 导出 (10) $7+ 0 ≤ 3 + 9$

(x1,y1 是 (6) 中的变量重命名， x2,y2,z2 是 (8)中的变量重命名)

从 (4), (10), (8) $\{x3/7,x4/7,y4/7+ 0,z4/3+ 9\}$ 导出 (11) 7 ≤ 3+ 9

(x3 是 (4)中的变量重命名， x4,y4,z4 是 (8)中的变量重命名)

## 9.24

### (a)

(A) 翻译为“对于任意自然数，存在小于等于它的自然数”

(B)翻译为“存在一个自然数，任意自然数都大于等于它”

### (b)

为真。

### (c)

为真。

### (d)

否。

### (e)

是。

### (f)

设 (B) 的否定为 (-B)

(A) $x \geq F_1(x)$

(-B) $\neg F_2(y) \geq y$

合一置换应该为 $\{x/F_2(y),y/F_1(x)\}$, 但等效于 $\{x/F_2(y),y/F_1(F_2(y))\}$, 因为 $y$ 是一个包含 $y$ 的表达式，所以解析失败。

### (g)

设 (A) 的否定为 (-A)

(A) $\neg F_1(y) \geq y$

(-B) $x \geq F_2(x)$

合一置换为 $\{x/F_1(y),y/F_2(x)\}$, 从而产生了假，证明 (B) 逻辑蕴含 $A$.
