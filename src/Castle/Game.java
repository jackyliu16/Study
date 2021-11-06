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

 */
import java.util.Scanner;

public class Game {
    private Room currentRoom;
        
    public Game() 
    {
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
    // 以下为用户命令

    private void printHelp() 
    {
        System.out.print("迷路了吗？你可以做的命令有：go bye help");
        System.out.println("如：\tgo east");
    }

    private void goRoom(String direction) 
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
		Scanner in = new Scanner(System.in);
		Game game = new Game();
		game.printWelcome();

        while ( true ) {
        		String line = in.nextLine();
        		String[] words = line.split(" ");
        		if ( words[0].equals("help") ) {
        			game.printHelp();
        		} else if (words[0].equals("go") ) {
        			game.goRoom(words[1]);
        		} else if ( words[0].equals("bye") ) {
        			break;
        		}
        }
        
        System.out.println("感谢您的光临。再见！");
        in.close();
	}

}
