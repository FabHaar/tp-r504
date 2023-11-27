import java.io.*;
import java.net.*;

public class ClientUDP
{
	public static void main ( String[] args )
	{
		try 
		{
			//Q1
			InetAddress addr = InetAddress.getLocalHost();
			System.out.println("adresse = " + addr.getHostName() );
		
			String s ="Hello World";
		
			byte[] data = s.getBytes(); 
		
			DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234);
			DatagramSocket sock = new DatagramSocket();
			sock.send(packet);
			
			//Q1.3
			System.out.println("-Waiting data back");
			DatagramPacket packetback = new DatagramPacket(new byte[1024], 1024);
			sock.receive(packetback);
			String str = new String(packet.getData() );
			System.out.println( "str back=" + str );
			sock.close();
		}
		catch (Exception ex) 
		{
			System.out.println("erreur !");
			ex.printStackTrace();
		}
	}
}
