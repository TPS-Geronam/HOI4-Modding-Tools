package main.java.core;

import main.java.modules.*;
import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.LineBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.net.URI;

public class Main {
    public static console con;

    public static void main(String[] arguments) throws Exception {
        con = new console();
        initiateWindow();

        System.out.println("Window initiated.");
    }

    public static void initiateWindow() {
        JFrame f = new JFrame("HoI4 Modding Tools");
        f.getContentPane().setLayout(new FlowLayout());

        //Duplicate Remover
        hoi4_removeduplicateloc remover = new hoi4_removeduplicateloc(f);
        f.add(remover.createButton());

        //Python
        python_scripts blanker = new python_scripts(f);
        f.add(blanker.createButton());

        //Console toggle
        JButton console_toggle = new JButton("Toggle console");
        console_toggle.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    con.setVisibility(!con.getVisibility());
                    System.out.println("Action: Console set to " + !con.getVisibility());
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });
        f.add(console_toggle);

        //Source link
        JLabel gitLink = new JLabel("<html><a href=''>Source available on GitHub</a></html>", JLabel.CENTER);
        gitLink.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    Desktop.getDesktop().browse(new URI("https://github.com/TPS-Geronam/HOI4-Modding-Tools"));
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
            @Override
            public void mouseEntered(MouseEvent e) {
                gitLink.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
            }
        });
        f.add(gitLink, BorderLayout.PAGE_END);

        f.pack();
        f.setResizable(false);
        f.setSize(200, 150);
        f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}