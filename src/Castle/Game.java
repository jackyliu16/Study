package castle;
/*
面向对象程序设计原则
    1. 消除代码复制
        修改方案，提取对应字符作为新的函数ShowPrompt()
    2. 通过封装来降低耦合(降低类之间的关联)
    > **在程序设计中，应当尽可能的维持所有的成员变量都是private的， 不到万不可以，不要使用public变量**

        对于本次的代码而言，Room和Game 两个类都有大量的代码相关(就比如说Game引用了大量Room中的public变量.
            而与此相类似的是在程序中书写一个getNorth的函数，然后通过return来返回对应的变量[基本上思维与上面类似，但是是private的]
        而在这个地方真正的思考方式是：
            为什么要通过Game来得到有什么出口，而不是通过Room提供对应的出口信息呢？这样就可以避免了Game对于Room的过多信息调用。

        在本次的操作中我们通过产生getExit() and getExitDesc()两个接口，
        降低了两个类之间的关联程度【一个类不会使用到另一个类中的变量】
        在此基础上，将方向的表示，尽可能的通过Room来完成
    3. 通过容器来实现灵活性
        Room的方向是通过成员变量进行表示的，增加或者减少方向都需要对于代码进行改动
        但如果通过Hash表来表示方向，那么方向就不是硬编码的了【方向与Room没有关系了】
        【硬编码是将数据直接嵌入到程序或其他可执行对象的源代码中的软件开发实践，与从外部获取数据或在运行时生成数据不同。】
    4.  以框架 + 数据来提高代码 的可扩展性
        对于Room进行改造，使原来【通过成员变量进行硬编码】，变成用容器。
        在Room中我们就创建了一个框架，也就是cmd和房间之间的对应关系
        思路：
        把程序尽可能的解成框架 + 数据的格式
        【在本次更新中主要通过Handler类来处理命令】
        用hash表来保存命令和Handler之间的关系【使命令解析脱离if-else的结构】
            [ 由于hash表要求的是key - value(二者都是对象),但是想要达到key-function]
            因此要通过类间接调用函数
        注意：相对于给出的代码，此处在Handler函数中还额外的对于Game函数进行了重写
        【不知道为什么之前会报栈溢出的错误，但是现在似乎莫名其妙的好了？】
 */
import java.util.HashMap;
import java.util.Scanner;

public class Game {
    private Room currentRoom;
    private HashMap< String, Handler> handlers = new HashMap<String,Handler>();
        
    public Game() 
    {
        handlers.put("go",new HandlerGo(this));
        handlers.put("bye",new HandlerBye(this));
        handlers.put("help",new HandlerHelp(this));
        createRooms();
    }

    private void createRooms()
    {
        Room outside, lobby, pub, study, bedroom;
      
        //	制造房间
        outside = new Room("城堡外");
        lobby = new Room("大堂");
        pub = new Room("小酒吧");
        study = new Room("书房");
        bedroom = new Room("卧室");
        
        //	初始化房间的出口
        outside.setExit("east", lobby);
        outside.setExit("south",study);
        outside.setExit("west",pub);
        lobby.setExit("west",outside);
        pub.setExit("east",outside);
        study.setExit("north",outside);
        study.setExit("east",bedroom);
        bedroom.setExit("west",study);
        lobby.setExit("up",pub);
        pub.setExit("down",lobby);

        currentRoom = outside;  //	从城堡门外开始
    }

    private void printWelcome() {
        System.out.println();
        System.out.println("欢迎来到城堡！");
        System.out.println("这是一个超级无聊的游戏。");
        System.out.println("如果需要帮助，请输入 'help' 。");
        System.out.println();
        showPrompt();
    }

    public void showPrompt(){
        System.out.println("现在你在" + currentRoom);
        System.out.print("出口有：");
        System.out.println(currentRoom.getExitDesc());
        System.out.println();
    }

    public void play(){
        Scanner in = new Scanner(System.in);
        while ( true ) {
            String line = in.nextLine();
            String[] words = line.split(" ");
            Handler handler = handlers.get(words[0]);
            String value = "";
            if ( words.length > 1 )
                value = words[1];
            if ( handler != null ){
                handler.doCmd(value);
                // 这个地方我感觉不是很正确，应当采用先后顺序法，
                // 先判断第一个是否bye然后再说别的，传输一个空的参数感觉还是有点危险
                if( handler.isBye() ){
                    break;
                }
            }

        }
        in.close();
    }
    // 以下为用户命令

    public void goRoom(String direction)
    {
        Room nextRoom = currentRoom.getExit(direction);
        if (nextRoom == null) {
            System.out.println("那里没有门！");
        }
        else {
            currentRoom = nextRoom;
            showPrompt();
        }
    }
	
	public static void main(String[] args) {

		Game game = new Game();
		game.printWelcome();
        game.play();

        
        System.out.println("感谢您的测试，再见！");

	}

}
