package leetcode.editor.cn;

import java.sql.Array;
import java.util.*;

public class Tools {
    // ========== 从此开始参考 https://zhuanlan.zhihu.com/p/360824190 ========== //

    public static int getTreeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        return 1 + Math.max(getTreeDepth(root.left), getTreeDepth(root.right));
    }

    private static String traversePreOrder(TreeNode root) {
        if (root == null) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        sb.append(root.val);

        String pointerRight = "└──";
        String pointerLeft;
        if (root.right != null) {
            pointerLeft = "├──";
        } else {
            pointerLeft = "└──";
        }

        traverseNodes(sb, "", pointerLeft, root.left, root.right != null);
        traverseNodes(sb, "", pointerRight, root.right, false);

        return sb.toString();
    }

    private static void traverseNodes(StringBuilder sb, String padding, String pointer, TreeNode node,
                                      boolean hasRightSibling) {
        if (node == null) {
            return;
        }

        sb.append("\n");
        sb.append(padding);
        sb.append(pointer);
        sb.append(node.val);

        StringBuilder paddingBuilder = new StringBuilder(padding);
        if (hasRightSibling) {
            paddingBuilder.append("│  ");
        } else {
            paddingBuilder.append("   ");
        }

        String paddingForBoth = paddingBuilder.toString();
        String pointerRight = "└──";
        String pointerLeft = (node.right != null) ? "├──" : "└──";

        traverseNodes(sb, paddingForBoth, pointerLeft, node.left, node.right != null);
        traverseNodes(sb, paddingForBoth, pointerRight, node.right, false);
    }

    public static void printTreeHorizontal(TreeNode root) {
        System.out.print(traversePreOrder(root));
    }

    // 实现斜树
    public static void printTree(TreeNode root) {
        int maxLevel = getTreeDepth(root);
        printNodeInternal(Collections.singletonList(root), 1, maxLevel);
    }

    private static void printNodeInternal(List<TreeNode> nodes, int level, int maxLevel) {
        if (nodes == null || nodes.isEmpty() || isAllElementsNull(nodes)) {
            return;
        }

        int floor = maxLevel - level;
        int endgeLines = (int) Math.pow(2, (Math.max(floor - 1, 0)));
        int firstSpaces = (int) Math.pow(2, (floor)) - 1;
        int betweenSpaces = (int) Math.pow(2, (floor + 1)) - 1;

        printWhitespaces(firstSpaces);

        List<TreeNode> newNodes = new ArrayList<TreeNode>();
        for (TreeNode node : nodes) {
            if (node != null) {
                System.out.print(node.val);
                newNodes.add(node.left);
                newNodes.add(node.right);
            } else {
                newNodes.add(null);
                newNodes.add(null);
                System.out.print(" ");
            }

            printWhitespaces(betweenSpaces);
        }
        System.out.println("");

        for (int i = 1; i <= endgeLines; i++) {
            for (int j = 0; j < nodes.size(); j++) {
                printWhitespaces(firstSpaces - i);
                if (nodes.get(j) == null) {
                    printWhitespaces(endgeLines + endgeLines + i + 1);
                    continue;
                }

                if (nodes.get(j).left != null) {
                    System.out.print("/");
                } else {
                    printWhitespaces(1);
                }

                printWhitespaces(i + i - 1);
                if (nodes.get(j).right != null) {
                    System.out.print("\\");
                } else {
                    printWhitespaces(1);
                }
                printWhitespaces(endgeLines + endgeLines - i);
            }

            System.out.println("");
        }

        printNodeInternal(newNodes, level + 1, maxLevel);
    }

    private static void printWhitespaces(int count) {
        for (int i = 0; i < count; i++) {
            System.out.print(" ");
        }
    }

    private static <T> boolean isAllElementsNull(List<T> list) {
        for (Object object : list) {
            if (object != null) {
                return false;
            }
        }

        return true;
    }

    // 从数组构建树
    public static TreeNode constructTree(Integer[] array) {
        if (array == null || array.length == 0 || array[0] == null) {
            return null;
        }

        int index = 0;
        int length = array.length;

        TreeNode root = new TreeNode(array[0]);
        Deque<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.offer(root);
        TreeNode currNode;
        while (index < length) {
            index++;
            if (index >= length) {
                return root;
            }
            currNode = nodeQueue.poll();
            Integer leftChild = array[index];
            if (leftChild != null) {
                currNode.left = new TreeNode(leftChild);
                nodeQueue.offer(currNode.left);
            }
            index++;
            if (index >= length) {
                return root;
            }
            Integer rightChild = array[index];
            if (rightChild != null) {
                currNode.right = new TreeNode(rightChild);
                nodeQueue.offer(currNode.right);
            }
        }

        return root;
    }

    // ========== 从此结束参考 https://zhuanlan.zhihu.com/p/360824190 ========== //

    public static TreeNode createTree(Integer...data){
        return constructTree(data);
    }

    public static int createNumberFromArray(int...data){
        int res = 0;
        for (int datum : data) {
            res *= 10;
            res += datum;
        }
        return res;
    }

    // Swap
    // 结果适用于任意实现了comparable接口的数据类型比如Integer and Double
    public static void swap(Comparable[] arr, int a, int b){
        // 本段代码参考自算法4-P153
        Comparable t = arr[a];
        arr[a] = arr[b];
        arr[b] = t;
    }

    public static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    public static void swap(short[] arr, int a, int b) {
        short temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    public static void swap(long[] arr, int a, int b) {
        long temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    public static void swap(boolean[] arr, int a, int b) {
        boolean temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    // Print of Arrays
    public static void print(boolean[] data) {
        for ( boolean k : data ) {
            if (k)
                System.out.print("1"+" ");
            else
                System.out.print("0"+" ");
        }
        System.out.println();
    }
    public static void print(int[] data) {
        for (int i : data) {
            System.out.print(i+"\t");
        }
        System.out.println();
    }
    public static void print(long[] data) {
        for (long i : data) {
            System.out.print(i+"\t");
        }
        System.out.println();
    }
    public static void print(String[] data) {
        for ( String k : data ) {
            System.out.print(k);
        }
        System.out.println();
    }
    public static void print(double[] data) {
        for ( double k : data ) {
            System.out.print(k);
        }
        System.out.println();
    }
    public static void print(char[] data) {
        for (char datum : data) {
            System.out.print(datum + "\t");
        }
        System.out.println();
    }

    public static void print(int[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
//		System.out.println();
    }
    public static void print(long[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void print(double[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void print(float[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();

    }
    public static void print(String[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();

    }
    public static void print(char[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void print(boolean[][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            print(data[i]);
            System.out.println();
        }
        System.out.println();
    }

    public static void print(String[][][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                for ( int k = 0 ; k < data[i][j].length ; k++ ) {
                    System.out.print(data[i][j][k]+" ");
                }
                System.out.println();
            }
            System.out.println("层数："+i);
        }
    }
    public static void print(int[][][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                for ( int k = 0 ; k < data[i][j].length ; k++ ) {
                    System.out.print(data[i][j][k]+" ");
                }
                System.out.println();
            }
            System.out.println("层数："+i);
        }
    }
    public static void print(long[][][] data) {
        for ( int i = 0 ; i < data.length ; i++ ) {
            for ( int j = 0 ; j < data[i].length ; j++ ) {
                for ( int k = 0 ; k < data[i][j].length ; k++ ) {
                    System.out.print(data[i][j][k]+" ");
                }
                System.out.println();
            }
            System.out.println("层数："+i);
        }
    }
    public static void main(String[] args) {
        Integer[] a = new Integer[]{1,2,3,4};
        swap(a,2,3);

    }
}
