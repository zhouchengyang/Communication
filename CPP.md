## C++
### Run
* 编译链接 g++ main.cpp -o main
* g++ main.cpp -std=c++11
* 运行可执行程序 ./main
### Basics Of language
* include<>表示编译器标准库 include"" 表示打开当前路径下的头文件
* using namespace name表示使用name命名空间，而不需要使用name::fun 类似于from name import *
* 标准C++由三个部分组成：核心语言、C++标准库、C++标准模板库（STL)
* 命名空间namespace可以理解为定义不同的仓库namespace1::fun1()
    * 定义：namespace namespace1{}，可以是定义新的，也可以是给原有的命名空间增加元素
    * 使用：namespace1::fun1()或者using namespace namespace1;多个文件下都能知道
* 常量：
    * 数字字符串常量
    * #define A value1预定义常量
    * const type name = value1定义常量
* 分号表示语句结束，语句块不需要加分号
* C++注释，//或者/**/
* 数据类型：自定义、内置、衍生类型
    * 基础类型bool char int float double(1,2,4,8字节) void, 可以加修饰符signed unsigned long short
    * 定义type name1, name2 = value2;
    * 重新定义typedef type name
* 运算符：
    * 算数运算符：+ - * / %
    * 赋值运算符：++ += -= /=
    * 逻辑运算符：&& || !
    * 关系运算符：== != > < >=
    * 三元运算符：number = (num == 10)?value1:value2 类似于number = value1 if num == number1 else value2
* 条件判断，if ,else if,else {}
* 选择判断，switch () {case val1: break;}
* 循环操作：
    * for(init; condition; increment){}
    * while(condition){sentence;}
    * continue 和 break
* 函数包括自定义以及内置函数：
    * return_type function_name(parameter_list) {}
    * 函数声明和函数定义
    * 默认参数的使用
    * 传入数组，传出数组
    * 函数传入形参的时候会自动产生副本
* 数组：
    * 定义数组：type name[length] 或者 type name[] = {value1, value2};
    * 多维数组：type name[length] [length1] 或者type name[][] = {{},{}}
    * 作为函数的输入以及输出
* 字符串：可以创建字符列表或者字符对象
    * string name1定义对象;
    * 类里面许多功能;
* 指针：本质上就是存储某一类数据地址的变量
    * 定义 int *p,var;
    * NULL指针其实是表示结束，标准库里面值为0的常量
    * 赋值 p = &var;
    * 指针和数组，数组名字本质上就是一个指针，指向了数组的最开始地址，但是不能对数组++，可以对指针++来循环数组里面的元素
* 引用：引用是某个变量的一个别名,必须在创建的时候初始化
    * 定义 int &name = varible1;
    * 引用相当于原始变量的别名，不占内存地址，与原变量是同一地址
    * 应用：引用作为参数，如果有大块的数据需要传递的话，采用指针，在Cpp中也可以采用引用。指针可读性差，用引用更方便。
    * 应用：如果需要提高引用的效率，又要保护不被改变，就应该使用常引用。const type &name = varible1;这样引用就不能修改，但是原本的变量可以被修改，尽量定义为const。
    * 应用：引用作为返回值，在内存中不产生返回值的副本，type &fun(){}  ,但是要求变量的引用不能是局部变量，因为局部变量在函数退出之后就会自动销毁。
    * 应用：type fun() const表示不改变成员函数。
* 输入输出：cin cout
* 数据结构：
    * struct type_name {} varible1定义;
    * 调用varible1.name = N;
    * 在定义和函数里面使用的时候type_name varible1;
### Object oriented programming
* 定义：class Name{public: private:}
* 构造函数，类创建的时候会自动执行的函数，子类创建的时候会自动调用父类函数
    * 不带参数的构造函数Line:Line(void)
    * 带参数的构造函数Line:Line(double len),也可以用初始化列表来初始化字段Line:Line(double len):length(len)表示类里面的变量length = len;父类必须用初始化列表进行初始化;自定义对象的类初始化也可以在初始化列表里面;
    * 拷贝构造函数，表示从另一个变量里面构造或者初始化对象classname(const classname &obj){},当一个类初始化等于同一个类的时候自动调用。在把对象传入函数或者从函数返回的时候会调用拷贝函数，利用另一个对象进行初始化的时候需要。
    * this指针可以使用表示当前的对象，this->member
* 静态成员：表示无论创建多少个对象的是还静态成员都只有一个副本;静态函数：跟类里面的成员没有关系，可以直接调用，classn::fun()
* 友元函数：友元函数可以访问类里面的私有变量。可以使用obj.mem1,例子friend void disp(const &XXX obj);
* 内联函数：内联函数似乎没特别的作用
* 虚函数：来实现多态，在不同的子类里面来自动判断输出的类型 纯虚函数
* 继承：class child:father,也可以有多个继承class child:father1,father2
### Advanced features
* 异常处理：throw, try{}catch(){}
* 动态内存：new data_type生成新内存的地址
* 预处理：也就是预定义，在真实的编译的时候替换成预定义的值
    * #ifdef #define # endif
### Standard Template Library
* STL抽象了4个部分，算法，容器，函数和迭代器
* 迭代器 
* #include <vector>
    * push back
### Question
* const
    * const主要是表示一旦定义完之后就不能改变，const type name = value，必须赋初值
    * const修饰指针变量及引用：int const*a = ;int *const a = ;int const &a = x;表示a不可改变，x可以改变。
    * 作为函数参数的const与变量定义相同;类中的成员函数后面加上const表示这个函数不会修改任何数据成员，函数前面加上const其实用处不大。
* static
* externl
* new
    * 主要表示是构造一个空间并且返回地址例如int *p = new int;int *p = new int(10);开辟一个存储空间并且赋值为10;
* shred_ptr是比较有用的一类指针，非常安全可靠
    * 定义shared_ptr<type> name;
* auto是可以自动推断数据类型的关键字
