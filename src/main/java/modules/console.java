package main.java.modules;

import javax.swing.*;
import java.awt.*;
import java.io.*;

public class console {
    JFrame frame;

    public console() {
        frame = new JFrame();
        frame.add( new JLabel("Action Console" ), BorderLayout.NORTH );

        JTextArea ta = new JTextArea();
        TextAreaOutputStream taos = new TextAreaOutputStream( ta, 60 );
        PrintStream ps = new PrintStream(taos);
        System.setOut( ps );
        System.setErr( ps );

        frame.add( new JScrollPane( ta )  );

        frame.pack();
        frame.setVisible( true );
        frame.setSize(500,300);
    }

    public void setVisibility(boolean val) {
        frame.setVisible(val);
    }

    public boolean getVisibility() {
        return frame.isVisible();
    }
}
