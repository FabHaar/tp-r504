import java.io.*;
import java.net.*;

public class ClientTCP2
{
	public static void main ( String[] args )
	{
		try
		{
			//q2.1 
			Socket socket = new Socket("localhost",2016);
			DataOutputStream dOut = new DataOutputStream(socket.getOutputStream() );
			dOut.writeUTF(args[0]); // Q2.2 choix du message à envoyer
			socket.close();
		}
		catch (Exception ex) 
		{
			System.out.println("erreur !");
			ex.printStackTrace();
		}
	}
}
