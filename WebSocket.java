import java.net.*;
import java.io.*;

public class WebSocket {

	public static void main(String[] args) throws IOException{
		ServerSocket ss =  new ServerSocket(4999);

		for(;;){
			Socket s = ss.accept();

			System.out.println("Client Connected");

			InputStreamReader in = new InputStreamReader(s.getInputStream());
			BufferedReader bf = new BufferedReader(in);

			String str = bf.readLine();
			System.out.println("client: "+str);
		} 

	}



}