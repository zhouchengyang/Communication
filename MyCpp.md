### Basic

* 编译是指将CPP转化为OBJ文件(机器语言，一一对应)，链接是指将多个OBJ连接到一起成为可执行文件

* cmake是将cmakelist文件转化为makefile文件，然后make是将源文件转化通过makefile转换为可执行文件

  ![img](https://img-blog.csdn.net/20180620083108405?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjQ5MTg1Nw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

* 可以定义：namespace AA{}，使用: AA::Fun()或者using namespace AA;
* const type define_var = value; constexpr define_var = value;(constexpr在编译期就能被确定值，简化过程)
* 定义类，变量，函数声明都需要分号，块语句，namespce，函数定义都不需要分号
* 数据类型：自定义、内置、衍生类型
* 引用与指针的功能，const的功能，左右值引用
  * 可以取地址的，有名字的，非临时的就是左值；
  * 不能取地址的，没有名字的，临时的就是右值；延长临时对象的使用周期
  * std::move()是将左值转化为右值引用
  
* 匿名函数： [] (parameter) -> return_type{} body只有“return”或者返回为void，那么”->return-type“可以被省去

### Oop

* 在C++中struct与class的区别仅仅是对权限的控制(struct是公有，class默认是私有)
  * 一般使用typedef struct structA{} A，牵扯到跟C语言的一些渊源
  * 初始化可以使用A a = {};
* Class A{}; 构造函数值得注意的是初始化列表;默认构造函数，拷贝构造函数，赋值运算符
* 值得注意的是：同一个类的不同对象之间是可以互相调用私有变量的，所以拷贝构造函数是可以调用另一个对象的私有变量的
* 内联函数:优点不需要像普通函数一样传递函数入栈出栈，节省
* default与delete：default是用于构造函数设置默认，delete是设置构造函数不可用
* 虚函数virtual fun = 0，继承class A: public B，基类的析构函数需要定义为虚函数
* 构造函数：默认构造函数在未定义其他构造函数时编译器会提供，也可使用default
* explicit是指取消构造函数的隐世转换 Like String A = "sdf";
* 内存泄漏是指在程序运行期间内存无法回收的情况new 出来的内存不删除
* 子类构造函数执行前会先调用父类构造函数，而在析构是会后调用父类析构函数(析构函数为虚函数的时候)

### STL Container

* Vector #include<vector>
  * Constructor vector(int n), vector(int n, const T&), vector(vector & b), vector(iterator begin, iterator end);
  * Size size(), capacity(),max_size(),clear()(表示size = 0),resize()(表示size = new_size), empty()，reserve()(可以改变capacity, 可以增大或者减小)
  * Add push_back(const T&), emplace_back(const T&), insert(iterator a, const T&),emplace(iterator a, const T&)
  * Delete erase(iterator b, iterator c)(删除[b, c)的元素), pop_back(), clear()
  * Assign v.swap(vector& b),assign(int n, const T&),assign(iterator a, iterator b)
* Array #include<array>
  * Construtor array<int, n> a;array<int, n> a = {};
  * Size size(), max_size()
  * Assign at(), fill(),front(),back()
* String #include<string>
  * Constructor string(string& s), string(string&s, i, j), string(char c, int n), string(string & s, int length)(选择length到最后的作为初值), string(C_str cs, int length)(选择0-length的作为初值)
  * Size size(), length(),capacity(),clear(),resize()
  * Add push_back(char c), insert(iterator it, char c), append(c_str or string, ) = +, assign(iterator a, iterator b),erase(iterator it, iterator it2),replace(iterator it1, iterator it2, s),c_str(), find(c_s, or string, begin_index, n) == std::string::npos, substr(i, j)
  * std::stoi(string), std::stof(string), std::to_string(float or int)
* Set #include<set>
  * Constructor set(set & s), set(iterator it, iterator it2)
  * Size size(), empty()
  * Add 只能insert()和emplace(),erase(), clear()
  * Range find(const T&), count(), pair = equal_range(),  lower_bound()
  * Multiset: 与set函数相同，但是能存储相同的值
  * For(auto it = se.begin(); it != se.end; ++it)
* Map #include<map>
  * Pair #include<utillity>
    * Costructor pair(a, b) pair a;
    * Assign p.first, p.second, make_pair(a, b)
  * Constructor map(const map& m), map(iterator it, iterator it2)
  * Size size(), empty(), clear()
  * Access at(key), [key], insert, erase(const& T),insert(const & T)
  * Range find, count, equal_range()
  * Multimap, 与map相同，但是可以存储相同的key
* Unordered_set  #include<unordered_set>
* Unordered_map #include<unordered_map>
* Ifstream, Ofstream #include<fstream>

### STL Algorithm

* all_of(iterator it1, iterator it2, fun), any_of, none_of, for_each(iterator it1, iterator it2, fun)
* find(iterator it1, iterator it2, element)->iterator, find_if, find_if_not
* count(iterator it1, iterator it2, element), count_if(iterator1, iterator2, fun)
* copy(from_iterator1, from_iterator2, to_iterator1), copy_n(), move(from_iterator1, from_iterator2, to_iterator1), move(a),
* transform(from_iterator1, from_iterator2, to_iterator1, fun), replace(iterator it1, iterator it2, value1, value2),replace_if(iterator it1, iterator it2, fun, value2)
* fill(iterator1, iterator2, value1), generate(iterator1, iterator2, fun), remove(iterator1, iterator2), remove_if, reverse(iterator1, iterator2), random_shuffle(iterator1, itertor2)
* sort(iterator1, iterator2, fun), min(a, b), min_element(iterator1, iterator2)

### Advanced

* #include<memory>

