import java.io.*;
import java.net.*;

public class ClientTCP1
{
	public static void main ( String[] args )
	{
		try
		{
			//q2.1 
			Socket socket = new Socket("localhost",2016);
			DataOutputStream dOut = new DataOutputStream(socket.getOutputStream() );
			dOut.writeUTF("message test");
			socket.close();
		}
		catch (Exception ex) 
		{
			System.out.println("erreur !");
			ex.printStackTrace();
		}
	}
}
