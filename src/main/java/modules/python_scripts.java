package main.java.modules;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class python_scripts {
    private String action;
    private Component parent;
    private String inputFile;
    private String outputDir;

    public python_scripts(Component parent) {
        this.action = "Open Python Scripts Dir";
        this.parent = parent;
        this.outputDir = "";
    }

    public JButton createButton() {
        final JFileChooser fc = new JFileChooser();
        JButton hoi4_remlocdup = new JButton(action);
        hoi4_remlocdup.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    System.out.println("Action: " + action);

                    work();
                } catch (Exception ex) {
                    System.out.println(ex);
                }
            }
        });
        return hoi4_remlocdup;
    }

    public void work() {
        try {
            Desktop.getDesktop().open(new File(outputDir + "res/python_scripts"));

            System.out.println(action + ": Done");
        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }
}