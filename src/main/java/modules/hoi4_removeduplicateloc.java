package main.java.modules;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.apache.commons.io.FileUtils;

import java.io.*;
import java.util.ArrayList;

public class hoi4_removeduplicateloc {
    private String action;
    private Component parent;
    private String inputFile;
    private String outputDir;

    public hoi4_removeduplicateloc(Component parent) {
        this.action = "Remove Loc Duplicates";
        this.parent = parent;
        this.inputFile = "";
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
                    fc.setFileSelectionMode(JFileChooser.FILES_ONLY);
                    fc.setDialogTitle("Select text.log:");
                    int returnVal = fc.showOpenDialog(parent);
                    if (returnVal == JFileChooser.APPROVE_OPTION) {
                        inputFile = fc.getSelectedFile().getAbsolutePath();
                    }

                    fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
                    fc.setDialogTitle("Select directory of loc:");
                    returnVal = fc.showOpenDialog(parent);
                    if (returnVal == JFileChooser.APPROVE_OPTION) {
                        outputDir = fc.getSelectedFile().getAbsolutePath();
                    }

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
            System.out.println(action + ": Reading input file");
            File f = new File(inputFile);
            java.util.List<String> lines = FileUtils.readLines(f, "UTF-8");

            java.util.List<String> keys = new ArrayList<String>();
            for (String line : lines) {
                if (line.contains("Duplicate localization found, key: ")) {
                    String currentKey = line.substring(line.indexOf("Duplicate localization found, key: ") + 35, line.indexOf(", file:"));
                    if (!keys.contains(currentKey)) {
                        keys.add(currentKey);
                    }
                }
            }

            File folder = new File(outputDir);
            File[] listOfFiles = folder.listFiles();
            for (String key : keys) {
                System.out.println(action + ": Current key " + key);
                for (File file : listOfFiles) {
                    boolean found = false;
                    java.util.List<String> fileContent = new ArrayList<>(FileUtils.readLines(file, "UTF-8"));

                    for (int i = 0; i < fileContent.size(); i++) {
                        if (fileContent.get(i).contains(key + ":") && !fileContent.get(i).contains("#" + key + ":")) {
                            System.out.println(action + ": Found key inside " + file.getName());
                            fileContent.set(i, "#" + key + ":" + fileContent.get(i).substring(fileContent.get(i).indexOf(key + ":") + key.length() + 1));
                            FileWriter fw = new FileWriter(file, false);
                            fw.write(String.join("\n", fileContent));
                            fw.close();
                            found = true;
                            break;
                        }
                    }
                    if (found) {
                        break;
                    }
                }
            }
            System.out.println(action + ": Done");
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}