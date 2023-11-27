import java.io.*;
import java.net.*;

public class ServeurTCP2
{
	public static void main ( String[] args )
	{
		try
		{
			
			ServerSocket socketserver = new ServerSocket(2016);
			
			while (true) //Q2.2 on met le code dans un while true
			{
				//Q2.1
				System.out.println("serveur en attente");
				Socket socket = socketserver.accept();
				System.out.println("Connexion d'un client");
			
				DataInputStream dIn = new DataInputStream(socket.getInputStream());
				System.out.println("Message : " + dIn.readUTF());
				socket.close();
				//socketserver.close(); enlevé pour la q2.2 aussi
			}
		}
		catch (Exception ex) 
		{
			System.out.println("erreur !");
			ex.printStackTrace();
		}
	}
}
